import cv2
import numpy as np


img = cv2.imread('img/img.jpg')

#img[:,:,0] =0  #BGR , making B channel 0
#img[:,:,2] =0 

img = cv2.resize(img, (256,256))

imgBlue = img[:,:,0]
imgGreen = img[:,:,1]
imgRed = img[:,:,2]

img_new = np.hstack((imgBlue, imgGreen, imgRed))


cv2.imshow('imageBGRT', img_new)
cv2.waitKey(0)
print(img_new.shape)
