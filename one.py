import pyautogui
import cv2
import aircv as ac
import os
import numpy as np
import time



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
def fight():
    for i in range(1, 100):
        pyautogui.keyDown("x")
        pyautogui.keyUp("x")
    # for i in range(1, 20):
    #     pyautogui.keyDown("up")
    #     pyautogui.keyUp("up")
    # for i in range(1, 5):
    #     pyautogui.keyDown("down")xxxxxxx
    #     pyautogui.keyUp("down")
    # for i in range(1, 5):
    #     pyautogui.keyDown("right")
    #     pyautogui.keyUp("right")

# pyautogui.moveTo(800,80)
# pyautogui.click(800,80)
# fight()

image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
imobj = ac.imread(os.path.join(os.getcwd(),'wupin.png'))

pos = ac.find_all_template(image, imobj, threshold=0.7, rgb=False, bgremove=False)
draw_circles(image, pos, (0, 255, 0), 4)
print(pos)
click(pos)

# pyautogui.moveTo(800,80)
# pyautogui.click(800,80)
# image = pyautogui.screenshot()
# image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
# imobj = ac.imread(os.path.join(os.getcwd(),'wenhao.png'))
#
# pos = ac.find_all_template(image, imobj, threshold=0.7, rgb=False, bgremove=False)
# draw_circles(image, pos, (0, 255, 0), 2)
# print(len(pos), pos)
#click(pos)
# pyautogui.keyDown("left")
# pyautogui.keyDown("left")
# pyautogui.keyDown("left")
# pyautogui.keyDown("left")
# pyautogui.keyDown("left")
# pyautogui.keyUp("left")
#
# pyautogui.keyDown("space")
# pyautogui.keyUp("space")


# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
#
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
#
#
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
#
#
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
#
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")
# pyautogui.keyDown("x")
# pyautogui.keyUp("x")