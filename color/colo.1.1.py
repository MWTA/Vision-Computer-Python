#coding: utf-8
#!/usr/bin/python

'''
@Author RodriguesFAS
@Date 07/10/2017
@Email <fasr@cin.ufpe.br> || <franciscosouzaacer@gmail.com>
@site <htpp://rodriguesfas.com.br>
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('../src/35008.jpg')
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



print(gray)

b,g,r = cv2.split(img)
print(b)
print(g)
print(r)


ret, thresh = cv2.threshold(gray,0,255, cv2.THRESH_BINARY_INV+ cv2.THRESH_OTSU)

plt.imshow(img)
plt.title('original image'),
plt.show()

plt.imshow(gray)
plt.title('gray image'),
plt.show()

plt.imshow(thresh)
plt.title('thresholded image'),
plt.show()


# noise removal
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)

plt.imshow(sure_bg)
plt.title('background image'),
plt.show()

# Finding sure foreground area
sure_fg = cv2.erode(opening,kernel,iterations=3)

plt.imshow(sure_fg)
plt.title('foreground image'),
plt.show()

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)


plt.imshow(unknown)
plt.title('boundary of the well'),
plt.show()

edge = cv2.Canny(img,75,200)
plt.imshow(edge)
plt.title('edge of the well'),
plt.show()