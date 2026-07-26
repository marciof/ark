# VirtualBox

https://www.virtualbox.org

_(Last checked: v7.2.6)_

## Fix _"Can't Enumerate USB Devices"_

1. [Upgrade from v6 to v7](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/installation.html#install-linux-performing): `apt install virtualbox`
2. [Install extension pack](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/configuring-virtualbox.html#install-ext-pack) for USB support: [^1] `apt install virtualbox-ext-pack`
3. [Add user to USB group](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/working-with-vms.html#usb-implementation-notes): [^2] `usermod -aG vboxusers $USER`
4. [Log out and log in to apply changes.](https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/Troubleshooting.html#ts_usb-linux) [^3]

[^1]: > _"In addition [...] USB support. This package contains special drivers for your Windows host that Oracle VirtualBox requires to fully support USB devices inside your virtual machines."_

[^2]: > _"On supported Linux hosts, Oracle VirtualBox accesses USB devices through special files in the file system. When Oracle VirtualBox is installed, these are made available to all users in the vboxusers system group. In order to be able to access USB from guest systems, make sure that you are a member of this group."_

[^3]: > _"If USB is not working on your Linux host, make sure that the current user is a member of the vboxusers group. Please remember that group membership does not take effect immediately but rather at the next login. If available, the newgrp command may avoid the need for a logout and login."_
