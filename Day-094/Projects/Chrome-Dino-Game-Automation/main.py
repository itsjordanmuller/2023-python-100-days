import time
import numpy as np
import pyautogui
from PIL import ImageGrab, ImageOps


class coordinates:
    replaybutton = (480, 300)
    dinosaur = (250, 300)


def restart():
    pyautogui.click(coordinates.replaybutton)
    pyautogui.keyDown("down")


def jump():
    pyautogui.keyUp("down")

    pyautogui.keyDown("space")
    time.sleep(0.08)
    pyautogui.keyUp("space")

    pyautogui.keyDown("down")
