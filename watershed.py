import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
 
img = cv.imread('img/coins.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

#separate background ,fixed boundry and gaps between coins.

kernel =np.ones((3,3),np.uint8)
opening = cv.morphologyEx(thresh,cv.MORPH_OPEN ,kernel , iterations=2)

sure_bg = cv.dilate(opening,kernel,iterations=2)

#sure foreground
dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)


sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg,sure_fg)


ret, markers = cv.connectedComponents(sure_fg)
markers = markers +1
markers[unknown==255] = 0

markers = cv.watershed(img,markers)
img[markers == -1] = [255,0,0]



titles =['images','thresh', 'opening', 'sure_bg', 'sure_fg','unknown']
images =[img, thresh, opening,sure_bg,sure_fg,unknown]


num_rows = 2
num_cols = (len(titles)+1 )// num_rows

for i in range(len(titles)):
    plt.subplot(num_rows,num_cols,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()