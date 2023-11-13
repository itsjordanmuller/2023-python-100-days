import time
import numpy as np
import pyautogui
from PIL import ImageGrab, ImageOps


class GameCoordinates:
    REPLAY_BUTTON = (480, 300)
    DINOSAUR = (250, 300)


def restart_game():
    pyautogui.click(GameCoordinates.REPLAY_BUTTON)
    pyautogui.keyDown("down")


def jump():
    pyautogui.keyUp("down")
    pyautogui.keyDown("space")
    time.sleep(0.08)
    pyautogui.keyUp("space")
    pyautogui.keyDown("down")


def check_box():
    box = (
        GameCoordinates.DINOSAUR[0] + 30,
        GameCoordinates.DINOSAUR[1],
        GameCoordinates.DINOSAUR[0] + 130,
        GameCoordinates.DINOSAUR[1] + 30,
    )
    image = ImageGrab.grab(box)
    gray_image = ImageOps.grayscale(image)
    array = np.array(gray_image.getcolors())
    print(array.sum())
    return array.sum()


def main():
    restart_game()
    check_value = check_box()
    while True:
        if check_box() != check_value:
            jump()
            time.sleep(0.05)


if __name__ == "__main__":
    main()
