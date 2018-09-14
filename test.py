import pyautogui
import time
import aircv as ac
import numpy as np
import cv2
import os
import ops_util

#pyautogui.moveTo(30, 30)
#pyautogui.click(30 ,30)
#pyautogui.keyDown("down",pause=0.01)
#pyautogui.keyDown("down",pause=0.01)
#pyautogui.keyDown("down",pause=0.01)
#pyautogui.keyDown("down",pause=0.01)

#pyautogui.keyUp("up")

print(os.getcwd())
#method = cv.CV_TM_SQDIFF_NORMED
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
method = eval(methods[5])
# Read the images from the file
image = pyautogui.screenshot()
#image = pyautogui.screenshot(region=(0,0, 300, 400))

image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
#image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

cv2.imshow('output',image)
cv2.waitKey(0)


small_image = cv2.imread(os.path.join(os.getcwd(), 'rubbish.png'))
#large_image = cv2.imread('C:\\Users\\PIG\\PycharmProjects\\ai\\bg.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('output',small_image)
cv2.waitKey(0)
pos = ac.find_template(image, small_image)
print(pos)

#result = cv2.matchTemplate(small_image, large_image, method)
#result = cv2.matchTemplate(small_image, large_image, eval('cv2.TM_SQDIFF_NORMED'))
#result = cv2.matchTemplate(small_image, image, eval('cv2.TM_SQDIFF_NORMED'))

#print(result)

# We want the minimum squared difference
#mn,_,mnLoc,_ = cv2.minMaxLoc(result)

# Draw the rectangle:
# Extract the coordinates of our best match
#MPx,MPy = mnLoc

# Step 2: Get the size of the template. This is the same size as the match.
#trows,tcols = small_image.shape[:2]

# Step 3: Draw the rectangle on large_image
#cv2.rectangle(image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# Display the original image with the rectangle around the match.
#cv2.imshow('output',image)

# The image is only displayed if we call this
#cv2.waitKey(0)

# this time take a screenshot directly to disk
#pyautogui.screenshot("straight_to_disk.png")

# we can then load our screenshot from disk in OpenCV format
#image = cv2.imread("straight_to_disk.png")
#cv2.imshow("Screenshot", imutils.resize(image, width=600))

if __name__ == '__main__':
    pass