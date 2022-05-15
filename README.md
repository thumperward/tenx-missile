# Tenx USB Missile Launcher Python Driver

This is a Python driver to control the Tenx USB Missile Launcher
(`0x1130`/`0x0202`).

It is tested in Python 3 and an Ubuntu based distro.

## Executing as non root

In order to connect to the USB without being a super user, you need to add a
`udev` rule.

As a super user, just create a new file `/etc/udev/rules.d/99-missile.rules`
with the following content:

```cfg
SUBSYSTEM=="usb", ATTR{idVendor}=="1130", ATTR{idProduct}=="0202", MODE="666"
```

Then, restart `udev` with:

```sh
sudo udevadm trigger
```

## TODO

-   Permit interactive use. This will mean exposing `_send_command()` directly
    so that the application can issue the `self._STOP` itself.

## Acknowledgements

-   <https://www.npmjs.com/package/tenx-usb-missile-launcher-driver>
-   <https://github.com/AlexNisnevich/sentinel>
-   <https://github.com/pddring/usb-missile-launcher>
