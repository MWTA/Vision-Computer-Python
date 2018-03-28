#coding: utf-8
#!/usr/bin/python

'''
@Author RodriguesFAS
@Date 09/10/2017
@Email <fasr@cin.ufpe.br> || <franciscosouzaacer@gmail.com>
@site <htpp://rodriguesfas.com.br>
'''

import cv2
import numpy as np

img_orig = cv2.imread('../src/35008.jpg')

img_gray = cv2.cvtColor(img_orig, cv2.COLOR_RGB2GRAY)

img_blur = cv2.medianBlur(img_gray, 5)

canny = cv2.Canny(img_blur, 50, 150)

_, contours,_ = cv2.findContours(canny.copy(), cv2.HOUGH_GRADIENT, cv2.CHAIN_APPROX_SIMPLE)

mask = np.full((img_orig.shape[0], img_orig.shape[1]), 0, dtype=np.uint8)

for c in contours:
	cv2.drawContours(mask, [c], 0, color=(255, 255, 255), thickness=10)

# get first masked value (foreground)
fg = cv2.bitwise_or(img_orig, img_orig, mask=mask)

# get second masked value (background) mask must be inverted
mask = cv2.bitwise_not(mask)
background = np.full(img_orig.shape, 0, dtype=np.uint8)
bk = cv2.bitwise_or(background, background, mask=mask)

# combine foreground+background
final = cv2.bitwise_or(fg, bk)

cv2.imshow('orig', img_orig)
cv2.imshow('canny', canny)
cv2.imshow('mask', mask)
cv2.imshow('result', final)

cv2.waitKey(0)