#coding: utf-8
#!/usr/bin/python

'''
REFERÊNCIAS:
	<http://acodigo.blogspot.com.br/2017/07/umbralizacion-en-opencv.html>

@Author RodriguesFAS
@Date 26/09/2017
@Email <fasr@cin.ufpe.br> || <franciscosouzaacer@gmail.com>
@site <htpp://rodriguesfas.com.br>

'''

# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np

src = '../src/parafuso_porca.bmp'

img_org = cv2.imread(src)

gray = cv2.imread(src, cv2.IMREAD_GRAYSCALE)

t, dst1 = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)
t, dst2 = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY_INV)
t, dst3 = cv2.threshold(gray, 170, 255, cv2.THRESH_TRUNC)
t, dst4 = cv2.threshold(gray, 170, 255, cv2.THRESH_TOZERO)
t, dst5 = cv2.threshold(gray, 170, 255, cv2.THRESH_TOZERO_INV)
t, dst6 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
t, dst7 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

cv2.imshow('original', img_org)
cv2.imshow('limiar', gray)
cv2.imshow('limiar binario', dst1)
cv2.imshow('limiar binario inverso', dst2)
cv2.imshow('truncar', dst3)
cv2.imshow('definir para zero', dst4)
cv2.imshow('inverta a configuracao de zero', dst5)
cv2.imshow('limiar otimo atomatico triangle', dst6)
cv2.imshow('limiar otimo atomatico otsu', dst7)

cv2.waitKey(0)

