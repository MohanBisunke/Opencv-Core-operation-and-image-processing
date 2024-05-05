import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('img/extremepoints.jpg')
imggray = cv2.imread('img/extremepoints.jpg' , cv2.IMREAD_GRAYSCALE)

canny = cv2.Canny(imggray,170,220)
coutours, heirarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #image, retrerival mode, approximation 


cv2.drawContours(img,coutours ,-1,(0,255,0),3)  #source , sequence(-1 means all counter else n means n-1 countours ), color ,thickness


cnt = coutours[0]
x,y,w,h = cv2.boundingRect(cnt)
aspect_ratio = float (w)/h
print(aspect_ratio)

area = cv2.contourArea(cnt)
x,y,w,h = cv2.boundingRect(cnt)
extent = float (area)/(w*h)
print(extent)

hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area
print(solidity)


leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

titles = ['img']
images =[img]
num_rows = 2
num_cols = (len(images) + 1) // num_rows

for i in range(len(titles)):
    plt.subplot(num_rows, num_cols,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()
    


