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

import cv2
import numpy as np

# opencv loads the image in BGR, convert it to RGB
img_orig = cv2.imread('../src/35008.jpg')

img_rgb = cv2.cvtColor(img_orig, cv2.COLOR_BGR2RGB)

img_gauss = cv2.GaussianBlur(img_rgb, (5, 5), 0)

lower_white = np.array([90, 90, 90], dtype=np.uint8)
upper_white = np.array([255, 255, 255], dtype=np.uint8)

mask = cv2.inRange(img_gauss, lower_white, upper_white)  # could also use threshold

cv2.imshow('mask', mask)

mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)))  # "erase" the small white points in the resulting mask
mask = cv2.bitwise_not(mask)  # invert mask

# load background (could be an image too)
bk = np.full(img_gauss.shape, 255, dtype=np.uint8)  # white bk

# get masked foreground
fg_masked = cv2.bitwise_and(img_gauss, img_gauss, mask=mask)

# get masked background, mask must be inverted 
mask = cv2.bitwise_not(mask)
bk_masked = cv2.bitwise_and(bk, bk, mask=mask)

# combine masked foreground and masked background 
final = cv2.bitwise_or(fg_masked, bk_masked)
mask = cv2.bitwise_not(mask)  # revert mask to original

cv2.imshow('result', final)

cv2.waitKey(0)


















