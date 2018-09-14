import sys
import os
import pyautogui
import screen
import logging
import cv2
import aircv as ac
import numpy as np

def resource_path(*relative):

    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, *relative)
    return os.path.join(os.getcwd(), *relative)

def capture_main():
    img=pyautogui.screenshot(region=(screen.Screen.X, screen.Screen.Y, screen.Screen.W, screen.Screen.D))
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    return img


def capture_param(x,y,w,d):
    img=pyautogui.screenshot(region=(screen.Screen.X+x, screen.Screen.Y+y, w, d))
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    return img

def capture_finish():
    img=pyautogui.screenshot(region=(screen.Screen.PX, screen.Screen.PY, screen.Screen.PW, screen.Screen.PD))
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    return img

def find_pos_main(*args, td = 0.7):
    img = capture_main()
    obj = ac.imread(resource_path(*args))
    pos = ac.find_all_template(img, obj, threshold=td)
    return pos

def find_pos_finish(*args, td = 0.65):
    img = capture_finish()
    obj = ac.imread(resource_path(*args))
    pos = ac.find_all_template(img, obj, threshold=td)
    return pos


def find_pos_param(x,y,w,d,*args, td = 0.65):
    img = capture_param(x,y,w,d)
    obj = ac.imread(resource_path(*args))
    pos = ac.find_all_template(img, obj, threshold=td)
    return pos

def test_log():
    logging.debug("%s", "in test log")