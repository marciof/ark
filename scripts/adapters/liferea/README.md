# Setup

## Plugin

### Linux

Symlink the provided plugin into the plugins folder:

```shell
ln -v -s "`realpath -e ext_cmd`" "`./path_to.py plugins`"
```

## Liferea

### Linux

Set the environment variable specified in the [`*.plugin` file](./ext_cmd/ext_cmd.plugin):

1. Create a file [setting the variable in a `~/.config/environment.d/*.conf` file](https://www.freedesktop.org/software/systemd/man/environment.d.html).
2. To apply changes:
   - **Either**, log out and log in.
   - **Or**, update the D-Bus activation environment with the variable above and restart Liferea.
     ```shell
     dbus-update-activation-environment --verbose --systemd [...]
     ```

> [!Important]
> `~/.config` may be located elsewhere, as per the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir/). [^xdg-config]

> [!Note]
> [`DBusActivatable=true` is set in Liferea's `*.desktop` file](https://github.com/search?q=repo%3Alwindolf%2Fliferea+path%3A**%2F*.desktop*+DBusActivatable), which means [environment variables defined there won't be passed along](https://developer.gnome.org/documentation/guidelines/maintainer/integrating.html#d-bus-activation). [^dbus-env-var]

> [!Tip]
> Set Liferea to [auto-start on login](https://specifications.freedesktop.org/autostart/):
> ```shell
> dpkg -L liferea | grep -F .desktop | xargs ln -v -s -t ~/.config/autostart/ 
> ```

[^dbus-env-var]: > _"If DBusActivatable is true and the desktop file name looks like a valid application ID, then the Exec line will be ignored and your application will be started by way of D-Bus activation instead (using the name of the desktop file minus the .desktop extension as the application ID)."_

[^xdg-config]: > _"There is a single base directory relative to which user-specific configuration files should be written [...] defined by the environment variable $XDG_CONFIG_HOME."_

### Windows

Liferea isn't available natively for Windows, so [install WSL first](https://learn.microsoft.com/windows/wsl/tutorials/gui-apps) to run it from within.

# Development

## Linux

Generate type stubs for `gi.repository.Liferea`:

```shell
dpkg -L liferea-data | grep -F .gir | xargs gengir --outdir ./stubs/gi
```

> [!Note]
> If necessary, [use `pyenv` to install an older Python version](https://github.com/pyenv/pyenv).
