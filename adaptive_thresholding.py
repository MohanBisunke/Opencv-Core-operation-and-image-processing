import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img/adaptive.png', cv2.IMREAD_GRAYSCALE)

_, th1 = cv2.threshold(img, 127,255,cv2.THRESH_BINARY)

threshold1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 3) 
#based on mean, thresh is calcualted from its blocksize (15)
threshold2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 3) 
#based on weighted mean, thresh is calcualted from its blocksize (15)




titles = ['Original Image','BINARY','Adaptive Mean' ,'Adaptive Gaussian']
images = [img, th1,  threshold1, threshold2, ]
 
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()

