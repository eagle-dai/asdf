import pyautogui
import time
import aircv as ac
import numpy as np
import cv2
import os
import logging
import screen
import kb_util
def clear_main_screen() -> None:
    kb_util.esc()



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    screen.Screen.init_dummp()
    screen.focus()
    clear_main_screen()



