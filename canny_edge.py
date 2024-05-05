import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('img/gradienttest.webp' ,cv2.IMREAD_GRAYSCALE)

canny = cv2.Canny(img,100,200)
canny2 = cv2.Canny(img, 80,200)
canny3 = cv2.Canny(img,50,200)
canny0 = cv2.Canny(img,0,200)



titles = ['image', 'canny100', 'canny80','canny50', 'canny0']
images =[img,canny,canny2,canny3, canny0]

num_rows = 2
num_cols = (len(images) + 1) // num_rows

for i in range(len(titles)):
    plt.subplot(num_rows, num_cols,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()