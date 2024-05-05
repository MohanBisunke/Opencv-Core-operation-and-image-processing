import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('img/gradienttest.webp')

imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imgx = cv2.imread('img/gradienttest.webp', cv2.IMREAD_GRAYSCALE)


ret, thresh = cv2.threshold(imggray, 127,255,0)
canny = cv2.Canny(imggray,170,220)
coutours, heirarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #image, retrerival mode, approximation 


cv2.drawContours(img,coutours ,-1,(0,255,0),3)  #source , sequence(-1 means all counter else n means n-1 countours ), color ,thickness

titles = ['img' , 'imggray', 'direct']
images =[img, imggray, imgx]
num_rows = 2
num_cols = (len(images) + 1) // num_rows

for i in range(len(titles)):
    plt.subplot(num_rows, num_cols,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()