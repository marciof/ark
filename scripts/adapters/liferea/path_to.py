#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Prints the path to a Liferea file/folder.

Paths to folders always end with the OS' path separator.

References:

- XDG Spec: https://specifications.freedesktop.org/basedir/latest/#variables
- Liferea man page: https://github.com/lwindolf/liferea/blob/v1.16.13/man/liferea.1
"""


# /// script
# dependencies = [
#   "platformdirs==4.11.0", # locate Liferea data/settings
# ]
# ///


# stdlib
import argparse
import os
from pathlib import Path
from typing import List, Optional, NoReturn

# external
import platformdirs


def get_feed_list_opml_path(app_name: str) -> Path:
    return (platformdirs.user_config_path(appname=app_name, appauthor=False)
        / 'feedlist.opml')


def get_plugins_path(app_name: str) -> Path:
    return (platformdirs.user_data_path(appname=app_name, appauthor=False)
        / 'plugins')


# TODO request Liferea cmdline flag to print paths
#      or via `gsettings list-recursively org.gnome.feed.Reader`
# FIXME tests (including mypy, pycodestyle)
# FIXME error handling
def main(args: Optional[List[str]] = None) -> NoReturn:
    arg_parser = argparse.ArgumentParser(description=__doc__.strip())
    cmd_parser = arg_parser.add_subparsers(required=True)

    opml_cmd = cmd_parser.add_parser('opml', help='feed list OPML file')
    opml_cmd.set_defaults(func=get_feed_list_opml_path)

    plugins_cmd = cmd_parser.add_parser('plugins', help='plugins folder')
    plugins_cmd.set_defaults(func=get_plugins_path)

    parsed_args = arg_parser.parse_args(args)
    path = parsed_args.func(app_name='liferea')

    if path.is_dir():
        # FIXME check if forcing a trailing separator is cross-platform
        path = str(path) + os.sep

    print(path)
    raise SystemExit()


if __name__ == '__main__':
    main()
