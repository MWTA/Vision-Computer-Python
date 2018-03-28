#coding: utf-8
#!/usr/bin/python

'''
@Author RodriguesFAS
@Date 29/09/2017
@Email <fasr@cin.ufpe.br> || <franciscosouzaacer@gmail.com>
@site <htpp://rodriguesfas.com.br>
'''

# Python 2/3 compatibility
from __future__ import print_function
import cv2
import numpy as np
 
# carregar as imagens
img1 = cv2.imread("../src/ESTEIRA0-300x225.jpg")
img2 = cv2.imread("../src/ESTEIRA1-300x225.jpg")
img3 = cv2.imread("../src/mask-300x225.jpg")
 
# convert the images for gray scale
imgray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
imgray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
imgray3 = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)

#find the diference betwen img1 and img2
diference = cv2.subtract(imgray1, imgray2)

cv2.imshow('DIFERENCA', diference)

# to turn white all pixels non-zero (binary image)
diference[diference > 0] = 255

# kernel to use in erode function
kernel = np.ones((2, 2), np.uint8)
 
# erode the noise
erode = cv2.erode(diference, kernel, iterations=2)
 
#show imagem in a window

#show imagem in a window
cv2.imshow('EROSAO', erode)
 
#wait any key to close the window
cv2.waitKey(0)