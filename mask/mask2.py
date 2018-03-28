import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('../src/35008.jpg')

# create a mask image of the same shape as input image, filled with 0s (black color)
mask = np.zeros_like(image)
rows, cols,_ = mask.shape

# create a white filled ellipse
mask = cv2.ellipse(mask, center=(rows/2, cols/2), axes=(100,100), angle=0, startAngle=0, endAngle=360, color=(255,255,255), thickness=-1)
cv2.imshow('mask', mask)


# Bitwise AND operation to black out regions outside the mask
result = np.bitwise_and(image,mask)


# Convert from BGR to RGB for displaying correctly in matplotlib
# Note that you needn't do this for displaying using OpenCV's imshow()
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
mask_rgb = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)
result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

# Plotting the results
#cv2.imshow('rgb', image_rgb)
#cv2.imshow('mask', mask_rgb)
#cv2.imshow('result', result_rgb)

cv2.waitKey(0)