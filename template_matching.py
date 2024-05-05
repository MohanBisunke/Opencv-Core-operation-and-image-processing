import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the grayscale image and the template
img = cv2.imread('img/ronaldo.webp', cv2.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
template = cv2.imread('img/template.png', cv2.IMREAD_GRAYSCALE)
assert template is not None, "file could not be read, check with os.path.exists()"
img2 = img.copy()

# Get the dimensions of the template
w, h = template.shape[::-1]

# All the 6 methods for comparison in a list
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

# Prepare to display results in a grid
titles = methods
images = []

# Iterate over each method
for meth in methods:
    img = img2.copy()
    method = meth

    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # Draw rectangle around the matched region
    cv2.rectangle(img, top_left, bottom_right, 255, 2)
    
    # Append the resulting image to the list for display
    images.append(img)

# Determine grid layout
num_rows = 2
num_cols = (len(images) + 1) // num_rows

# Display the results in a grid
for i in range(len(titles)):
    plt.subplot(num_rows, num_cols, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
