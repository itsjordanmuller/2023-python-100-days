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


def checkBox():
    box = (
        coordinates.dinosaur[0] + 30,
        coordinates.dinosaur[1],
        coordinates.dinosaur[0] + 130,
        coordinates.dinosaur[1] + 30,
    )

    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)

    array = np.array(grayImage.getcolors())

    print(array.sum())
    return array.sum()
