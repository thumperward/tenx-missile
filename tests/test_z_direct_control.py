from tenx_missile import MissileLauncher
import time


def test_direct_control():
    m = MissileLauncher()
    # m.send_command("DOWN")
    time.sleep(3)
    m.send_command("STOP")
    time.sleep(3)
    m.send_command("UP")
    time.sleep(3)
    m.send_command("STOP")
    time.sleep(1.5)
    m.send_command("FIRE")
