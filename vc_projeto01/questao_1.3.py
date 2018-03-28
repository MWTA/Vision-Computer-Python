#coding: utf-8
#!/usr/bin/python

'''
@Author RodriguesFAS
@Date 07/09/2017
@Email <fasr@cin.ufpe.br> || <franciscosouzaacer@gmail.com>
@site <htpp://rodriguesfas.com.br>
'''

# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np

img_base = cv2.imread('../src/parafuso_porca.bmp')
img_alvo = cv2.imread('../src/objetos.bmp')

gray_img_base = cv2.cvtColor(img_base, cv2.COLOR_BGR2GRAY)
gray_img_alvo = cv2.cvtColor(img_alvo, cv2.COLOR_BGR2GRAY)

t_base, dst_base = cv2.threshold(gray_img_base, 0, 255, cv2.THRESH_TRIANGLE)
t_alvo, dst_alvo = cv2.threshold(gray_img_alvo, 0, 255, cv2.THRESH_TRIANGLE)

_, contours_base, _ = cv2.findContours(dst_base, cv2.CHAIN_APPROX_NONE, cv2.RETR_LIST)
_, contours_alvo, _ = cv2.findContours(dst_alvo, cv2.CHAIN_APPROX_NONE, cv2.RETR_LIST)

parafuso_base = 0
porca_base = 0

for c in contours_base:
    area = cv2.contourArea(c)

    if area > 2500 and area < 10000:
    	porca_base = area
        cv2.drawContours(img_base, [c], 0, (0, 255, 0), 2, cv2.LINE_AA)

    if area > 10000 and area < 35000:
    	parafuso_base = area
    	cv2.drawContours(img_base, [c], 0, (0, 255, 0), 2, cv2.LINE_AA)

contPar = 0
contPor = 0

erroPar = 10600
erroPor = 3000

for c in contours_alvo:
    area = cv2.contourArea(c)

    if area > parafuso_base - erroPar and area < parafuso_base + erroPar:
    	cv2.drawContours(img_alvo, [c], 0, (0, 255, 0), 2, cv2.LINE_AA)
        contPar+=1

    elif area > porca_base - erroPor and area < porca_base + erroPor:
    	cv2.drawContours(img_alvo, [c], 0, (0, 255, 0), 2, cv2.LINE_AA)
        contPor+=1

print("{} Parafuso(s)".format(contPar))
print("{} Porca(s)".format(contPor))

cv2.imshow('Img Base', img_base)
cv2.imshow('Img Alvo', img_alvo)

cv2.waitKey(0)