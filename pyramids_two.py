import cv2 as cv,sys
import numpy as np
import matplotlib.pyplot as plt


A = cv.imread('img/apple.jpg')
B = cv.imread('img/orange.webp')
assert A is not None, "file could not be read, check with os.path.exists()"
assert B is not None, "file could not be read, check with os.path.exists()"
 
# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpA.append(G)
 
# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpA[i])
    GE = cv.resize(GE, (gpA[i - 1].shape[1], gpA[i - 1].shape[0]))
    L = cv.subtract(gpA[i-1],GE)
    lpA.append(L)
 
# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpB[i])
    GE = cv.resize(GE, (gpB[i - 1].shape[1], gpB[i - 1].shape[0]))
    L = cv.subtract(gpB[i-1],GE)
    lpB.append(L)
 
# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
    
    min_rows = min(la.shape[0], lb.shape[0])
    la_resized = cv.resize(la, (la.shape[1], min_rows))
    lb_resized = cv.resize(lb, (lb.shape[1], min_rows))

    # Concatenate the resized images horizontally
    ls = np.hstack((la_resized[:, :la_resized.shape[1] // 2], lb_resized[:, lb_resized.shape[1] // 2:]))
    LS.append(ls)
 
# now reconstruct
ls_ = LS[0]
for i in range(1,6):
    
    # Upsample the previous level in the Laplacian pyramid
    ls_ = cv.pyrUp(ls_)
    # Resize ls_ to match the dimensions of LS[i]
    ls_ = cv.resize(ls_, (LS[i].shape[1], LS[i].shape[0]))
    # Perform addition
    ls_ = cv.add(ls_, LS[i])

    
 
# Resize A and B to have the same number of rows
rows_A, cols_A, _ = A.shape
rows_B, cols_B, _ = B.shape
min_rows = min(rows_A, rows_B)
A_resized = cv.resize(A, (cols_A, min_rows))
B_resized = cv.resize(B, (cols_B, min_rows))

# Concatenate the resized images horizontally
real = np.hstack((A_resized[:, :cols_A // 2], B_resized[:, cols_B // 2:]))

cv.imwrite('img/Pyramid_blending2.jpg',ls_)
cv.imwrite('img/Direct_blending.jpg',real)