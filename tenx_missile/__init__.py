import time
import usb.core
import usb.util


class MissileLauncher(object):
    _VENDOR_ID = 0x1130
    _PRODUCT_ID = 0x0202

    _CMD_FILL = [0x00] * 56
    _commands = {
        "STOP": [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x08],
        "LEFT": [0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x08, 0x08],
        "RIGHT": [0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x08, 0x08],
        "UP": [0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x08, 0x08],
        "DOWN": [0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x08, 0x08],
        "UPLEFT": [0x00, 0x01, 0x00, 0x01, 0x00, 0x00, 0x08, 0x08],
        "UPRIGHT": [0x00, 0x00, 0x01, 0x01, 0x00, 0x00, 0x08, 0x08],
        "DOWNLEFT": [0x00, 0x01, 0x00, 0x00, 0x01, 0x00, 0x08, 0x08],
        "DOWNRIGHT": [0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0x08, 0x08],
        "FIRE": [0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x08, 0x08],
    }

    def __init__(self):
        self._device = usb.core.find(
            idVendor=self._VENDOR_ID, idProduct=self._PRODUCT_ID
        )
        if self._device is None:
            raise ValueError("Missile Launcher not found. Is it connected?")

        def _get_interface(num):
            # TODO: kernel drive check is Linux-only
            # if self._device.is_kernel_driver_active(num):
            #     self._device.detach_kernel_driver(num)
            usb.util.claim_interface(self._device, num)
            usb.util.release_interface(self._device, num)

        _get_interface(0)
        _get_interface(1)
        self._device.set_configuration()

    def left(self, ms=500):
        self.send_timed_command("LEFT", ms)

    def right(self, ms=500):
        self.send_timed_command("RIGHT", ms)

    def up(self, ms=500):
        self.send_timed_command("UP", ms)

    def down(self, ms=500):
        self.send_timed_command("DOWN", ms)

    def upleft(self, ms=500):
        self.send_timed_command("UPLEFT", ms)

    def downleft(self, ms=500):
        self.send_timed_command("DOWNLEFT", ms)

    def upright(self, ms=500):
        self.send_timed_command("UPRIGHT", ms)

    def downright(self, ms=500):
        self.send_timed_command("DOWNRIGHT", ms)

    def fire(self):
        self.send_command("FIRE")

    def stop(self):
        self.send_command("STOP")

    def send_timed_command(self, command, ms=500):
        self.send_command(command)
        time.sleep(ms / 1000)
        self.stop()

    def send_command(self, command):
        # ord('U'), ord('S'), ord('B'), ord('C') => 85, 83, 66, 67
        self._device.ctrl_transfer(
            0x21, 0x09, 0x2, 0x01, [85, 83, 66, 67, 0, 0, 4, 0]
        )
        self._device.ctrl_transfer(
            0x21, 0x09, 0x2, 0x01, [85, 83, 66, 67, 0, 64, 2, 0]
        )
        self._device.ctrl_transfer(
            0x21, 0x09, 0x2, 0x00, self._commands[command] + self._CMD_FILL
        )
