from tenx_missile import MissileLauncher
import time


def test_fire():
    m = MissileLauncher()
    time.sleep(2)
    m.right(1500)
    time.sleep(2)
    m.down(1500)
    time.sleep(2)
    m.up(1500)
    time.sleep(2)
    m.fire()
    time.sleep(6)
