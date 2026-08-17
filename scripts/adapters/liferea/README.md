# Setup

<!-- TODO how to test in clean environments?

- check CI? GitHub actions, Travis

- https://github.com/89luca89/distrobox
- https://www.vagrantup.com

- https://libvirt.org
- https://distrobox.it/posts/run_libvirt_in_distrobox/

- https://linuxcontainers.org
- https://www.freedesktop.org/software/systemd/man/latest/systemd-nspawn.html
- https://katacontainers.io
- https://github.com/firecracker-microvm/firecracker
- https://github.com/lima-vm/lima

- https://github.com/asweigart/pyautogui
- https://fedoramagazine.org/automation-through-accessibility/
-->

## Plugin

### Dependencies

None, other than what Liferea provides, but helper scripts may have their own, specified as inline script metadata [^pep-723] that can be installed using:

```shell
pip install --requirements-from-script [...]
```

> [!Note]
> Requires [pip v26.0](https://pip.pypa.io/en/stable/news/#v26-0) minimum.

[^pep-723]: [PEP 723 – Inline script metadata](https://peps.python.org/pep-0723/)

### Linux

<!-- TODO add setup for Windows? -->

Ensure the plugins folder exists:

```shell
./path_to.py plugins | xargs mkdir -v -p
```

Symlink the provided plugin into it:

```shell
ln -v -s "`realpath -e ./ext_cmd`" "`./path_to.py plugins`"
```

## Liferea

Set the environment variable specified in the [`*.plugin` file](./ext_cmd/ext_cmd.plugin).

### Linux

1. Create a file [setting the variable in a `~/.config/environment.d/*.conf` file](https://www.freedesktop.org/software/systemd/man/environment.d.html), for example:
   ```ini
   LIFEREA_ON_DOWNLOAD_URL=/path/to/scripts/events/download-url
   ```
2. To apply changes:
   - **Either**, log out and log in.
   - **Or**, update the D-Bus activation environment with the variable above and restart Liferea.
     ```shell
     dbus-update-activation-environment --verbose --systemd LIFEREA_ON_DOWNLOAD_URL=...
     ```

> [!Important]
> `~/.config` may be located elsewhere, as per the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir/). [^xdg-config]

> [!Note]
> [`DBusActivatable=true` is set in Liferea's `*.desktop` file](https://github.com/search?q=repo%3Alwindolf%2Fliferea+path%3A**%2F*.desktop*+DBusActivatable), which means [environment variables defined there will be ignored](https://developer.gnome.org/documentation/guidelines/maintainer/integrating.html#d-bus-activation). [^dbus-env-var]

> [!Tip]
> Set Liferea to [auto-start on login](https://specifications.freedesktop.org/autostart/):
> ```shell
> dpkg -L liferea | grep -F .desktop | xargs ln -v -s -t ~/.config/autostart/ 
> ```

[^dbus-env-var]: > _"If DBusActivatable is true and the desktop file name looks like a valid application ID, then the Exec line will be ignored and your application will be started by way of D-Bus activation instead (using the name of the desktop file minus the .desktop extension as the application ID)."_

[^xdg-config]: > _"There is a single base directory relative to which user-specific configuration files should be written [...] defined by the environment variable $XDG_CONFIG_HOME."_

### Windows

<!-- TODO fix WSLg + fast boot making Liferea's window disappear -->

Liferea isn't available natively for Windows, so [install WSL first](https://learn.microsoft.com/windows/wsl/tutorials/gui-apps) to then install and run it from within.

1. Shutdown WSL:
   ```batch
   wsl --shutdown
   ```
2. Open the `Environment Variables` window:
   ```batch
   rundll32 sysdm.cpl,EditEnvironmentVariables
   ```
3. Under `User variables` add the following:
   - `WSLENV`: `LIFEREA_ON_DOWNLOAD_URL/p` [^wsl-fs]
   - `LIFEREA_ON_DOWNLOAD_URL`: `C:\path\to\scripts\events\download-url` [^wsl-env]

> [!Important]
> Liferea may fail to open URLs in the external browser outside WSL, so configure its browser selection:
>
> 1. Install `xdg-utils`:
>    ```
>    apt install xdg-utils
>    ```
> 2. Go to `Preferences`, then `Browser`, then `External Browser Settings`.
> 3. Set `Manual` to  `xdg-open %s`.

[^wsl-fs]: [Working across Windows and Linux file systems](https://learn.microsoft.com/en-us/windows/wsl/filesystems)

[^wsl-env]: [Share Environment Vars between WSL and Windows](https://devblogs.microsoft.com/commandline/share-environment-vars-between-wsl-and-windows/)

# Development

## Linux

Generate type stubs for `gi.repository.Liferea`:

```shell
dpkg -L liferea-data | grep -F .gir | xargs gengir --outdir ./stubs/gi
```

> [!Note]
> If necessary, [use `pyenv` to install an older Python version](https://github.com/pyenv/pyenv).
