import pyautogui
import time
import aircv as ac
import numpy as np
import cv2
import os
import logging


def skill(s, n=1, delay=0.02):
    for i in range(0, n):
        pyautogui.keyDown(s, 0.05)
        pyautogui.keyUp(s, delay)


def esc(n=1, delay=0.02):
    for i in range(0,n):
        pyautogui.keyDown("esc", 0.05)
        pyautogui.keyUp("esc", delay)


def enter(n=1, delay=0.02):
    for i in range(0,n):
        pyautogui.keyDown("enter", 0.05)
        pyautogui.keyUp("enter", delay)

def space(n=1, delay=0.02):
    for i in range(0,n):
        pyautogui.keyDown("space", 0.05)
        pyautogui.keyUp("space", delay)


def left(n=1, delay=0.02):
    for i in range(0, n):
        pyautogui.keyDown("left", delay)
    pyautogui.keyUp("left", delay)


def right(n=1, delay=0.02):
    for i in range(0, n):
        pyautogui.keyDown("right", delay)
    pyautogui.keyUp("right", delay)


def up(n=1, delay=0.02):
    for i in range(0, n):
        pyautogui.keyDown("up", delay)
    pyautogui.keyUp("up", delay)


def down(n=1, delay=0.02):
    for i in range(0, n):
        pyautogui.keyDown("down", delay)
    pyautogui.keyUp("down", delay)


def right_run(n=1, delay=0.02):
    for i in range(0, n):
        pyautogui.keyDown("right", delay)
        pyautogui.keyUp("right", delay)


def up_run(n=1, delay=0.02):
    for i in range(0, n):
        pyautogui.keyDown("up", delay)
        pyautogui.keyUp("up", delay)


def f1(n=1, delay=0.02):
    for i in range(0, n):
        pyautogui.keyDown("f1", 0.05)
        pyautogui.keyUp("f1", delay)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    left()



