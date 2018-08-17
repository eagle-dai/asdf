import pyautogui
import time
import aircv as ac
import numpy as np
import cv2
import os
import logging
import screen
import kb_util
def process() -> None:
    kb_util.space()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    screen.Screen.init()
    screen.focus()
    process()



