import pyautogui
import time
import aircv as ac
import numpy as np
import cv2
import os
import logging
import ms_util
import ops_util
import mcfg
import gcf

def gen_speed():
    ops_util.up_v2(200)
    time.sleep(0.5)
    pos1 = None
    pos2 = None
    while gcf.Gcfg.running:
        pos1 = ops_util.find_my_pos()
        if len(pos1) == 1:
            break
    s = time.time()
    while gcf.Gcfg.running:
        pyautogui.keyDown("down", 0.05)
        if time.time() - s >= 1:
            break
    pyautogui.keyUp("down", 0.01)
    time.sleep(0.5)
    while gcf.Gcfg.running:
        pos2 = ops_util.find_my_pos()
        if len(pos2) == 1:
            break

    # 225,150,150,120,1.5,1.25
    logging.info("speed Y:%f", pos2[0]['result'][1] - pos1[0]['result'][1])
    mcfg.SPEED_Y = pos2[0]['result'][1] - pos1[0]['result'][1]
    mcfg.SPEED_X = mcfg.SPEED_Y * 1.5

class Screen(object):
    X = 0
    Y = 0
    W = 0
    D = 0
    PX = 0
    PY = 0
    PW = 0
    PD = 0
    DOWN = 406
    UP = 218

    def __init__(self):
        pass

    @staticmethod
    def init():
        img = pyautogui.screenshot()
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        obj = cv2.imread(ops_util.resource_path('screen', 'top.png'))
        pos = ac.find_all_template(img, obj, threshold=0.7, rgb=False, bgremove=False)
        logging.debug(pos)
        assert len(pos) >= 1
        Screen.X, Screen.Y = pos[0]['rectangle'][0]
        Screen.W, Screen.D = 800, 600
        Screen.PX, Screen.PY = Screen.X + 650, Screen.Y
        Screen.PW, Screen.PD = Screen.W - 650, 100
        logging.info('%d %d %d %d %d %d %d %d', Screen.X, Screen.Y, Screen.W, Screen.D, Screen.PX, Screen.PY, Screen.PW, Screen.PD)

    @staticmethod
    def init_dummp():
        # Screen.X,Screen.Y = 600, 150
        # (667, 29, 126, 126)
        Screen.X,Screen.Y = 1751, 705
        Screen.W, Screen.D = 800, 600
        Screen.PX, Screen.PY = Screen.X + 667, Screen.Y+29
        Screen.PW, Screen.PD = 126, 126
        logging.info('%d %d %d %d %d %d %d %d', Screen.X, Screen.Y, Screen.W, Screen.D, Screen.PX, Screen.PY, Screen.PW, Screen.PD)


def focus():
    ms_util.click(400, 25)

def focus_v2():
    ms_util.click(400, 25)

def direction(pos):
    # if pos[0]['result'][0] < 250:
    if pos[0]['result'][0] < 120:
        return 0

    if pos[0]['result'][0] > 700:
    # if pos[0]['result'][0] > 550:
        return 2

    if pos[0]['result'][1] < 440:
        return 1

    if pos[0]['result'][1] > 440:
        return 3

    return -1


def show(img, pos):
    for p in pos:
        cv2.rectangle(img, p["rectangle"][0], p["rectangle"][3], (0, 255, 0), 2)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    Screen.init()
    # exit(0)
    # Screen.init_dummp()
    focus()
    # Screen.gen_speed()



