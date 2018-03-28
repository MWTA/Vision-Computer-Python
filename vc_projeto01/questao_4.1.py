#coding: utf-8
#!/usr/bin/python

'''
@Author RodriguesFAS
@Date 06/10/2017
@Email <fasr@cin.ufpe.br> || <franciscosouzaacer@gmail.com>
@site <htpp://rodriguesfas.com.br>
'''

# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np

img_orig = cv2.imread('../src/predio.bmp')
cv2.imshow('Imagem Original', img_orig)

img_gray = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)

img_edges = cv2.Canny(img_gray, 3, 210, apertureSize = 3)

lines = cv2.HoughLinesP(img_edges, 1, np.pi/180, 90, minLineLength = 110, maxLineGap = 2)

contAndar = 0

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img_orig, (x1, y1), (x2, y2), (0, 0, 255), 2, cv2.LINE_AA)
    contAndar+=1

print("O prédio tem {} andar(es)".format(contAndar))

cv2.imshow('Detecao de Bordas Canny', img_edges)
cv2.imshow('Deteccao Linhas Hough', img_orig)

cv2.waitKey(0)

