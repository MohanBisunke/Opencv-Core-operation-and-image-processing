import cv2
import numpy as np

img = cv2.imread('img/img.jpg')
print(img.shape)



img_new = img[0:500,0:600]


cv2.imwrite('img/crop_img.jpg' ,img_new)
cv2.imshow('window' ,img_new)
cv2.waitKey(0)