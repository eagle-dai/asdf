import pyautogui
import time
import aircv as ac
import numpy as np
import cv2
import os
import logging
import screen

def move(x, y):
    pyautogui.moveTo(screen.Screen.X + x, screen.Screen.Y + y)


def click(x, y):
    for i in range(0,1):
        pyautogui.mouseDown(screen.Screen.X + x, screen.Screen.Y + y, button='left',_pause=True)
    for i in range(0,1):
        pyautogui.mouseUp(screen.Screen.X + x, screen.Screen.Y + y, button='left',_pause=True)
    time.sleep(0.2)


def click_down(x, y):
    for i in range(0,1):
        pyautogui.mouseDown(screen.Screen.X + x, screen.Screen.Y + y, button='left',_pause=True)
    time.sleep(0.2)

def click_up(x, y):
    for i in range(0,1):
        pyautogui.mouseUp(screen.Screen.X + x, screen.Screen.Y + y, button='left',_pause=False)
    time.sleep(0.2)

def click_first(pos):
    click(pos[0]['result'][0], pos[0]['result'][1])

def click_first_down(pos):
    click_down(pos[0]['result'][0], pos[0]['result'][1])

def click_one(p):
    click(p['result'][0], p['result'][1])

def click_first_right(pos):
    right_click(pos[0]['result'][0], pos[0]['result'][1])


def right_click(x,y):
    pyautogui.mouseDown(screen.Screen.X + x, screen.Screen.Y + y, button='right')
    pyautogui.mouseUp(screen.Screen.X + x, screen.Screen.Y + y, button='right')
    time.sleep(0.2)

def move(x,y):
    pyautogui.moveTo(screen.Screen.X + x,screen.Screen.Y + y)


def move_and_click(x,y):
    pyautogui.moveTo(screen.Screen.X + x,screen.Screen.Y + y)
    pyautogui.click(screen.Screen.X + x,screen.Screen.Y + y)
    # pyautogui.click(screen.Screen.X + x+33,screen.Screen.Y + y+44)
    # pyautogui.click()
    # pyautogui.click()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)



