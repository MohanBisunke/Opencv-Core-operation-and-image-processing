import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img/balls.webp' , cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img,127,255, cv2.THRESH_BINARY_INV)

kernel = np.ones((2,2), np.uint8)

dilation1 = cv2.dilate(mask,kernel)
dilation2 = cv2.dilate(mask, kernel, iterations=2)


kernel2 = np.ones((10,10), np.uint8)
dilation3 = cv2.dilate(mask, kernel2, iterations=2)

erosion1 = cv2.erode(mask, kernel, iterations=1)

opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,kernel)


titles = ['images','thresh_binary','dilation1' , 'erosion1', 'opening', 'closing']
images = [img, mask, dilation1, erosion1, opening, closing]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()
    