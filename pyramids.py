import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img/gradienttest.webp' ,cv2.IMREAD_GRAYSCALE)

lower_reso = cv2.pyrDown(img)
lower_reso2 =cv2.pyrDown(lower_reso)
lower_reso3 =cv2.pyrDown(lower_reso2)
lower_reso4 =cv2.pyrDown(lower_reso3)

titles =['a', 'b','c','d']
images = [lower_reso,lower_reso2,lower_reso3,lower_reso4]



num_rows = 2
num_cols = (len(images) + 1) // num_rows

for i in range(len(titles)):
    plt.subplot(num_rows, num_cols,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()