#coding: utf-8
#!/usr/bin/python

'''
REFERÊNCIAS:
	<http://acodigo.blogspot.com.br/2017/08/umbralizacion-adaptativa-con-opencv.html>

@Author RodriguesFAS
@Date 27/09/2017
@Email <fasr@cin.ufpe.br> || <franciscosouzaacer@gmail.com>
@site <htpp://rodriguesfas.com.br>

'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2

gray = cv2.imread('../src/sudoku.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Limiar', gray)

# Limiar Fixo
_, dst1 = cv2.threshold(gray, 96, 255, cv2.THRESH_BINARY)

cv2.imshow('Limiar Fixo', dst1)

# Limiar adaptativo
gray = cv2.medianBlur(gray, 5)
dst2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('Limiar Adaptativo', dst2)

cv2.waitKey(0)

