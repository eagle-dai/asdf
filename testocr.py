import tesserocr
from PIL import Image
import time
import cv2
import numpy
import PIL.ImageOps

print(tesserocr.tesseract_version())  # print tesseract-ocr version
print(tesserocr.get_languages()) # prints tessdata path and list of available languages

image = Image.open('ocr9.png')
image = image.convert('L')
image = PIL.ImageOps.invert(image)
image = image.convert('1')
image.save('new_name.png')


# img = cv2.cvtColor(numpy.asarray(image), cv2.COLOR_RGB2GRAY)
# image = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_GRAY2RGB))


s = time.time()
print(tesserocr.image_to_text(image, 'chi_sim'))  # print ocr text from image
print(tesserocr.image_to_text(image, 'chi_sim'))  # print ocr text from image
print(tesserocr.image_to_text(image, 'chi_sim'))  # print ocr text from image
print(tesserocr.image_to_text(image, 'chi_sim'))  # print ocr text from image
print(time.time() - s)


