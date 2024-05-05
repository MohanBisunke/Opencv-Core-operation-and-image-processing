import cv2
import numpy as np


#reading image

img = cv2.imread('img/img.jpg')
print(type(img))
print(img.shape)

#image display 

#cv2.imshow('window-name', img)
#cv2.waitKey(0)

#change to grayscale

gray_image = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

cv2.imshow('windows' ,gray_image)
cv2.waitKey(0)

print(gray_image.shape)
