from tenx_missile import MissileLauncher
import time


def test_fire():
    print("left")
    m = MissileLauncher()
    m.left(1500)
    time.sleep(2)
    print("right")
    m.right(1500)
    time.sleep(2)
    print("down")
    m.down(1500)
    time.sleep(2)
    print("up")
    m.up(1500)
    time.sleep(2)
    m.fire()
    time.sleep(5)
