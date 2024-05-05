import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img/gradient.jpg')


    
    
_, threshold1 = cv2.threshold(img, 155, 255, cv2.THRESH_BINARY)  # if pixel value less than 155 to zero(0) and greater to 255(1)
_, threshold2 = cv2.threshold(img, 155, 255, cv2.THRESH_BINARY_INV)  # inverse of threshold binary
_, threshold3 = cv2.threshold(img, 155, 255, cv2.THRESH_TRUNC)  # no change till threshold and then remains in threshold value.
_, threshold4 = cv2.threshold(img, 155, 255, cv2.THRESH_TOZERO)  # value below threshold to zero, else remains same
_, threshold5 = cv2.threshold(img, 155, 255, cv2.THRESH_TOZERO_INV)


titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, threshold1, threshold2, threshold3, threshold4, threshold5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
    
