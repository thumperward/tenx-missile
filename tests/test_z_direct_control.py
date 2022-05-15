from tenx_missile import MissileLauncher
import time


def test_direct_control():
    m = MissileLauncher()
    m.send_command([0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x08, 0x08])  # down
    time.sleep(3)
    m.send_command([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x08])  # stop
    time.sleep(3)
    m.send_command([0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x08, 0x08])  # up
    time.sleep(3)
    m.send_command([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x08])  # stop
    time.sleep(1.5)
    m.send_command([0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x08, 0x08])  # fire
