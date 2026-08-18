# -*- coding: UTF-8 -*-

"""
Plugin that runs external commands on various events.

Supported Events
================

Enclosure Download
------------------

Reinstates the external downloader tool functionality that was removed in
`v1.15.9 <https://github.com/lwindolf/liferea/releases/tag/v1.15.9>`_, by using
an environment variable to specify what command to run, with an enclosure URL
as its only argument.

Optionally, also disables the built-in download manager to prevent conflicts
and potential repeated downloads.

Motivation
^^^^^^^^^^

Using external downloaders with potentially wider support for various websites
(eg. `yt-dlp <https://github.com/yt-dlp/yt-dlp>`_), as well as more
powerful/flexible download management tools and GUIs.

Rationale
^^^^^^^^^

- A single command avoids complexity and bugs from shell parsing and un/quoting.
- Symlinks aren't cross-platform and aren't portable.
- Not all VCS' support symlinks.
- Avoids polluting `$PATH`, and it's also too implicit.
- Environment variables can be VCS-ed as "Configuration as Code".
- Protocol handler registration (eg. `extcmd://`) is too involved.
- An environment variable allows easier temporary changes.
"""


# TODO error handling
# TODO tests (+ mypy + pycodestyle)
# TODO document (+ dependencies + setup)

# TODO rename env var to "download enclosure"
# TODO could setup be simpler w/ sandboxing an old fixed version?
# TODO could setup be simpler w/ a `./ext_cmd.d/*` style folder?
#   - for Windows it could be just dropping a `.lnk` shortcut file
#   - `.gitignore` within `./download-enclosure/*`?

# TODO helper script to get an RSS feed URL from a YouTube channel/playlist?
#   - https://codemadness.org/sfeed.html
#   - check what/how Liferea does it

# TODO need to find alternatives to Liferea? it removed the external downloader
#   tool option (on v1.15.9), and may remove features currently in use, make
#   things more complicated, etc?
#   - RSS Guard, https://github.com/martinrotter/rssguard/issues/1952
#   - Akregator, https://github.com/KDE/akregator
#   - Alligator, https://github.com/kde/alligator
#   - Thunderbird, https://reviewers.addons.thunderbird.net/en-us/thunderbird/tag/rss
#   - local proxy (as done previously) as a hook for detecting enclosures,
#     and optionally downloading and passing on as a stream to the upstream app
#     https://github.com/yt-dlp/yt-dlp/wiki/FAQ#how-do-i-stream-directly-to-media-player


# stdlib
import configparser
from functools import partial
import logging
import os
from pathlib import Path
import subprocess
from threading import Thread
from typing import Callable, Generator, Optional, TextIO

# internal
import gi
gi.require_version('Peas', '2')
from gi.repository import Gio, GObject, Liferea, Peas


# TODO not logging to syslog from within WSL
# TODO seems to be missing from inside Liferea, but outside the plugin
# TODO use level from `$ liferea --help-debug`?
logging.basicConfig()


# TODO bring back the `Gio` alternative to avoid depending on dev pkgs?
# TODO document/handle missing dev pkgs: `apt install gir1.2-peas-2`
#   see: https://github.com/lwindolf/liferea/blob/v1.16.7/plugins/trayicon.py
class LifereaPlugins:

    """
    References:

    - https://gnome.pages.gitlab.gnome.org/libpeas/libpeas-2/
    """

    def __init__(self, logger: logging.Logger):
        self.logger = logger
        self.engine = Peas.Engine.get_default()


    def list_active(self) -> set[str]:
        # TODO does plugin order matter?
        return set(self.engine.dup_loaded_plugins())


    def disable(self, name: str) -> None:
        self.logger.info('Disabling plugin: %s', name)
        plugin = self.engine.get_plugin_info('download-manager')

        if plugin is None:
            self.logger.error('Plugin not found: %s', name)
        else:
            self.engine.unload_plugin(plugin)


# TODO refactor out config handling?
# TODO refactor out d-bus handling?
# TODO see LibnotifyPlugin for QoL ideas to notify user of errors
#      https://github.com/lwindolf/liferea/blob/v1.16.13/plugins/libnotify.py
class ExtCmdPlugin (

        GObject.Object,
        Liferea.Activatable, # Required by `DownloadActivatable`.
        Liferea.DownloadActivatable):

    """
    References:

    - https://github.com/lwindolf/liferea/blob/v1.16.13/plugins/README.md#plugin-tutorial
    - https://github.com/lwindolf/liferea/blob/v1.16.13/plugins/download-manager.py
    - https://github.com/lwindolf/liferea/blob/v1.16.13/src/plugins/download_activatable.c
    - https://github.com/mozbugbox/liferea-plugin-studio
    - https://api.pygobject.gnome.org/GObject-2.0/index.html
    """

    type ConfigKey = str | tuple[str, type[str | bool]]

    __gtype_name__ = __qualname__

    # Required by `DownloadActivatable`, even if not used:
    #   gi/types.py: Warning: Object class [PLUGIN] doesn't implement property
    #   'shell' from interface 'LifereaDownloadActivatable'
    shell = GObject.property(type=Liferea.Shell)


    # TODO instantiated twice at app startup?
    def __init__(self):
        super().__init__()

        plugin_path: Path = Path(__file__)
        plugin_name: str = plugin_path.stem

        self.logger: logging.Logger = logging.getLogger('plugin.' + plugin_name)
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug('__init__: %s', plugin_path)

        self.plugin_info_path = plugin_path.parent / (plugin_name + '.plugin')
        self.config_parser = configparser.ConfigParser()

        # TODO warn at startup if the env var is not defined
        self.logger.debug(
            'Config: on-download URL env var: $%s',
            '='.join(map(str, self.get_on_download_url_config())))

        self.logger.debug(
            'Config: disable download manager plugin? %s',
            '='.join(map(str, self.get_download_manager_config())))

        self.plugins = LifereaPlugins(self.logger)
        self.logger.debug('Active plugins: %s', self.plugins.list_active())

        app: Optional[Gio.Application] = Gio.Application.get_default()
        app_flags: Optional[Gio.ApplicationFlags] = (
            app.get_flags() if app is not None else None)

        # See https://api.pygobject.gnome.org/Gio-2.0/enum-ApplicationFlags.html#gi.repository.Gio.ApplicationFlags.IS_SERVICE
        # See https://dbus.freedesktop.org/doc/dbus-specification.html
        # See https://developer.gnome.org/documentation/guidelines/maintainer/integrating.html#d-bus-activation
        self.is_dbus_activatable: bool = (
            app_flags is not None
            and (app_flags & Gio.ApplicationFlags.IS_SERVICE) != 0)

        self.logger.debug(
            'D-Bus Activatable? %s; flags=%s',
            self.is_dbus_activatable,
            bin(app_flags) if app_flags is not None else None)


    def get_config(self, key: ConfigKey, *keys: ConfigKey) \
            -> Generator[Optional[str | bool]]:

        """
        References:

        - https://gnome.pages.gitlab.gnome.org/libpeas/libpeas-2/class.PluginInfo.html
        - https://docs.gtk.org/glib/struct.KeyFile.html
        """

        self.config_parser.read(self.plugin_info_path)
        section_name = 'Configuration'

        get_value_by_type = {
            str: partial(self.config_parser.get, section=section_name),
            bool: partial(self.config_parser.getboolean, section=section_name),
        }

        for key_name_type in (key,) + keys:
            if isinstance(key_name_type, str):
                key_name_type = (key_name_type, str)

            (key_name, key_type) = key_name_type
            yield get_value_by_type[key_type](option=key_name, fallback=None)


    def get_on_download_url_config(self) \
            -> tuple[Optional[str], Optional[str]]:

        (env_var,) = self.get_config('OnDownloadUrlEnvVar')

        if env_var is None:
            return (None, None)
        else:
            return (env_var, os.getenv(env_var))


    def get_download_manager_config(self) \
            -> tuple[Optional[str], Optional[bool]]:

        return self.get_config(
            'DownloadManagerPlugin',
            ('DisableDownloadManagerPlugin', bool))


    # TODO use `@override`?
    # inherit Liferea.Activatable
    def do_activate(self) -> None:
        self.logger.info('Activate')

        (plugin_name, should_disable) = self.get_download_manager_config()
        self.logger.info('Disable "%s" plugin? %s', plugin_name, should_disable)

        if should_disable:
            self.plugins.disable(plugin_name)


    # TODO use `@override`?
    # inherit Liferea.Activatable
    def do_deactivate(self) -> None:
        self.logger.info('Deactivate')


    # TODO use `@override`?
    # TODO how to handle importing a large feedlist.opml with encAutoDownload?
    # TODO Liferea sometimes not always updating some feeds even w/ new content
    #   (eg. TVW The Impact)
    # TODO feed fetch spacing option like RSS Guard? to avoid rate-limiting
    #   https://github.com/lwindolf/liferea/issues/1555
    # inherit Liferea.DownloadActivatable
    def do_download(self, url: str) -> None:
        # TODO wasteful to re-read config on all downloads -- watch cfg changes?
        (env_var, command) = self.get_on_download_url_config()

        if command is not None:
            self.logger.info('Download command=%s; url=%s', command, url)
            self.run_ext_cmd([command, url])
        else:
            # TODO separation of concerns, this belongs in the env var lookup
            self.logger.error(
                'Download aborted: $%s not set: looked in %s',
                env_var,
                sorted(os.environ.keys()))

            if self.is_dbus_activatable:
                self.logger.info(
                    'D-Bus Activatable detected. See README for help.',
                    env_var)


    def run_ext_cmd(self, command: list[str]) -> None:
        process = subprocess.Popen(command,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

        self.logger.info('Run pid=%s', process.pid)

        def log_output(pipe: TextIO, log: Callable[[str], None]) -> None:
            with pipe:
                for line in pipe:
                    log(line)

        def log_exit() -> None:
            code = process.wait()
            log = (self.logger.info if code == os.EX_OK else self.logger.error)
            log('Run pid=%s; exit=%s', process.pid, code)

        Thread(target=log_output, args=[
            process.stdout,
            partial(self.logger.info, f'[{process.pid}] %s'),
        ]).start()

        Thread(target=log_output, args=[
            process.stderr,
            partial(self.logger.error, f'[{process.pid}] %s'),
        ]).start()

        Thread(target=log_exit).start()
