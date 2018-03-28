#coding: utf-8
#!/usr/bin/python

'''
@Author RodriguesFAS
@Date 08/09/2017
@Email <fasr@cin.ufpe.br> || <franciscosouzaacer@gmail.com>
@site <htpp://rodriguesfas.com.br>
'''

# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np

img_orig = cv2.imread('../src/35008.jpg')

height, width = img_orig.shape[:2]

mask = np.zeros(img_orig.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (10, 10, width-15, height - 15)
cv2.grabCut(img_orig, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask = np.where((mask == 2)|(mask == 0), 0, 1).astype('uint8')
img_process = img_orig * mask[:, :, np.newaxis]

cv2.imshow('IMG ORIG', img_orig)
cv2.imshow('IMG SEGMENTADA', img_process)

cv2.waitKey(0)
