#coding: utf-8
#!/usr/bin/python
# Python 2/3 compatibility

import cv2
import numpy as np
import scipy.ndimage as ndimage

image = cv2.imread("../src/01.jpg", 0)

bimage = cv2.GaussianBlur(image, (3, 3), 0)
edge_image = cv2.Canny(bimage, 107, 208, apertureSize=3, L2gradient=False)
cv2.imshow('edge image', edge_image)

img2 = cv2.dilate(edge_image, np.ones((3, 3)), iterations=1)
cv2.imshow('dilate', img2)

dis_image = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
cv2.imshow('result1', dis_image)

labels, count = ndimage.label(img2)

for lab, idx in enumerate(ndimage.find_objects(labels.astype(int)), 1):
    sy = idx[0].start
    sx = idx[1].start
    y, x = np.where(labels[idx] == lab)
    ellp = cv2.fitEllipse(np.column_stack((x+sx, y+sy)))
    cv2.ellipse(dis_image, ellp, (0, 0, 255))

cv2.imshow('result', dis_image)

cv2.waitKey(0)
cv2.destroyAllWindows()