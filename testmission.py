import pyautogui
import cv2
import aircv as ac
import os
import numpy as np
import ops_util

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

# pyautogui.moveTo(30, 30)
#image = pyautogui.screenshot(region=(0,0, 1280, 800))
# image = pyautogui.screenshot()
# print(image.size)
# image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
image = ac.imread(ops_util.resource_path('task','start.png'))
imobj = ac.imread(ops_util.resource_path('task','m.png'))

pos = ac.find_all_template(image, imobj, threshold=0.9, rgb=False, bgremove=False)
print(len(pos), pos)
color = (0, 255, 0)
line_width = 1
draw_circles(image, pos, color, line_width)