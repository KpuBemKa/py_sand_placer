import win32com.client as comclt
import time
import os
from pynput.keyboard import Key, Controller as KeyboardController, Listener
from pynput.mouse import Button, Controller as MouseController


# block select key; default is mouse middle button
SELECT_BLOCK_KEY: Button = Button.x1
PLAYER_NAME = "cverti"


keyboard = KeyboardController()
mouse = MouseController()


def on_press(key):
    if key == Key.f6:
        keyboard.release("s")
        keyboard.press("w")
        time.sleep(100 / 1000)
        keyboard.release("w")

        keyboard.release(Key.shift_l)
        mouse.release(Button.right)
        mouse.release(SELECT_BLOCK_KEY)

        os._exit(0)


wsh = comclt.Dispatch("WScript.Shell")
wsh.AppActivate(f"Excalibur-Craft {PLAYER_NAME}")  # select another application

keyboard.press(Key.shift_l)
keyboard.press("s")
mouse.press(Button.right)

Listener(on_press=on_press).start()

while True:
    mouse.click(SELECT_BLOCK_KEY)
    time.sleep(1)
