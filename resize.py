import cv2
import numpy as np

img = cv2.imread('img/img.jpg')
print(img.shape)

img_resize = cv2.resize(img, (256,256))

print(img_resize.shape)
