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
from matplotlib import pyplot as plt

FONTE = cv2.FONT_HERSHEY_SIMPLEX
porcas = 0
parafusos = 0

img_orig = cv2.imread('../src/parafuso_porca.bmp')
cv2.imshow('IMG ORIG', img_orig)

ret, img_bin = cv2.threshold(img_orig, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('THRESH_BINARY_INV', img_bin)

gauss = cv2.GaussianBlur(img_bin, (5, 5), 0)
cv2.imshow('GAUSSIAN BLUR', gauss)

img_bin_gray = cv2.cvtColor(gauss, cv2.COLOR_BGR2GRAY)
cv2.imshow('COLOR_BGR2GRAY', img_bin_gray)

img, cont, hier = cv2.findContours(img_bin_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for c in cont:
    perimetro = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * perimetro, True)
    cv2.drawContours(img_bin, [c], -1, (0, 255, 0), 1)
    x, y, w, h = cv2.boundingRect(c)

    if len(approx) == 3 or len(approx) == 4:
        forma = "Parafuso"
        parafusos+=1

    elif len(approx) == 6:
        forma = "Porca"
        porcas+=1

    cv2.putText(img_bin, forma,(x, y), FONTE, 0.5,(0, 255, 0), 1, cv2.LINE_AA)

print("Foi encontrado {} parafuso(s)".format(parafusos))
print("Foi encontrado {} porca(s)".format(porcas))

cv2.imshow('RESULTADO QUESTAO 01', img_bin)

cv2.waitKey(0)