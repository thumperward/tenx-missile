from tenx_missile import MissileLauncher
import time


m = MissileLauncher()
m.left(1500)
time.sleep(2)
m.right(1500)
time.sleep(2)
m.down(1500)
time.sleep(2)
m.up(1500)
time.sleep(2)
m.fire()
