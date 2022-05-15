# Tenx USB Missile Launcher Python Driver

This is a Python driver to control the Tenx USB Missile Launcher
(`0x1130`/`0x0202`).

It is tested in Python 3 and an Ubuntu based distro.

## Setup

Project dependencies can be installed with Poetry.

In order to connect to the device without being a super user, you need to add a
`udev` rule. As a super user, just create a new file
`/etc/udev/rules.d/99-missile.rules` with the following content:

```cfg
SUBSYSTEM=="usb", ATTR{idVendor}=="1130", ATTR{idProduct}=="0202", MODE="666"
```

Then, restart `udev` with:

```sh
sudo udevadm trigger
```

## Usage

To initialise the device, import the library and create a `missileLauncher()`:

```python
from tenx_missile import MissileLauncher
m = MissileLauncher()
```

The following methods are pre-defined:

-   `left(ms=500)`
-   `right(ms=500)`
-   `up(ms=500)`
-   `down(ms=500)`
-   `upleft(ms=500)`
-   `upright(ms=500)`
-   `downleft(ms=500)`
-   `downright(ms=500)`
-   `fire()`

For the movement commands, the launcher will stop moving after `ms`
milliseconds.

In addition, the launcher can be sent timed directions directly using the
`send_timed_command(command, ms=500)` method, where `command` is the direction
(as an uppercase string, e.g. `"DOWNLEFT"`) and `ms` is the duration in
milliseconds.

Lastly, the launcher can operate in direct mode, using `send_command(command)`.
This method will not stop the launcher automatically: instead it must be
instructed to stop using the `stop()` or `send_command("STOP")` methods.

## Testing

Run `poetry run pytest`.

## TODO

-   ~Permit interactive use. This will mean exposing `_send_command()` directly
    so that the application can issue the `self._STOP` itself.~
-   Add an interactive app (keyboard and gui) which can be used to directly
    control the launcher.

## Acknowledgements

-   <https://www.npmjs.com/package/tenx-usb-missile-launcher-driver>
-   <https://github.com/AlexNisnevich/sentinel>
-   <https://github.com/pddring/usb-missile-launcher>
