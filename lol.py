import pyautogui
import cv2
import aircv as ac
import os
import numpy as np
import time


def draw_circle(img, pos, circle_radius, color, line_width):
    cv2.circle(img, pos, circle_radius, color, line_width)
    cv2.imshow('objDetect', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def draw_circles(img, res, color, line_width):
    for r in res:
        cv2.rectangle(img, r["rectangle"][0], r["rectangle"][3], color, thickness=line_width)
    cv2.imshow('objDetect', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def click(pos):
    for p in pos:
        pyautogui.moveTo(p["result"])

        pyautogui.mouseDown()
        pyautogui.mouseUp()



pyautogui.moveTo(1, 1)
#image = pyautogui.screenshot(region=(0,0, 1280, 800))
image = pyautogui.screenshot()
print(image.size)
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
imobj = ac.imread(os.path.join(os.getcwd(),'confirm.png'))
pos = ac.find_template(image, imobj)
pos = ac.find_all_template(image, imobj, threshold=0.7, rgb=False, bgremove=False)
print(len(pos), pos)
#draw_circles(image, pos, (0, 255, 0), 4)
 #click(pos)
pyautogui.moveTo(800,80)
pyautogui.click(800,80)
pyautogui.keyDown("esc")
pyautogui.keyUp("up")

time.sleep(0.5)
image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
imobj = ac.imread(os.path.join(os.getcwd(),'home.png'))

pos = ac.find_all_template(image, imobj, threshold=0.7, rgb=False, bgremove=False)
#draw_circles(image, pos, (0, 255, 0), 4)
print(pos)
click(pos)

pyautogui.keyDown("f12")
pyautogui.keyUp("f12")

pyautogui.keyDown("space")
pyautogui.keyUp("space")