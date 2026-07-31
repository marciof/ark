# Setup

## Plugin

Either copy, or symlink the provided plugin into the plugins folder:

```shell
ln -v -s "`realpath -e ext_cmd`" "`./path_to.py plugins`"
```

## Liferea

Set the environment variable specified in the [`*.plugin` file](./ext_cmd/ext_cmd.plugin):

<!-- TODO use XDG (or Python platformdirs?) for paths -->

1. Create a file [setting the variable in `~/.config/environment.d/*.conf`](https://www.freedesktop.org/software/systemd/man/latest/environment.d.html).
2. Log out and log in to apply changes.

> [!Important]
> If `DBusActivatable=true` is set in Liferea's `*.desktop` file, then [environment variables defined there won't be passed along](https://developer.gnome.org/documentation/guidelines/maintainer/integrating.html#d-bus-activation). [^dbus-env-var]

[^dbus-env-var]: > _"If DBusActivatable is true and the desktop file name looks like a valid application ID, then the Exec line will be ignored and your application will be started by way of D-Bus activation instead (using the name of the desktop file minus the .desktop extension as the application ID)."_

# Development

Generate type stubs for `gi.repository.Liferea`:

```shell
dpkg -L liferea-data | grep -F .gir | xargs gengir --outdir ./stubs/gi
```

> [!Note]
> If necessary, [use `pyenv` to install an older Python version](https://github.com/pyenv/pyenv).
