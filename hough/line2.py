#coding: utf-8
#!/usr/bin/python

'''
REFERÊNCIAS:
	<http://acodigo.blogspot.com.br/2017/09/deteccion-de-lineas-y-circulos-usando.html>

@Author RodriguesFAS
@Date 26/09/2017
@Email <fasr@cin.ufpe.br> || <franciscosouzaacer@gmail.com>
@site <htpp://rodriguesfas.com.br>

'''

# Python 2/3 compatibility

import cv2
import numpy as np

img = cv2.imread('../src/predio.bmp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize = 3)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 1, cv2.LINE_AA)

cv2.imshow('Bordas da Imagem', edges)
cv2.imshow('Detector de Linhas', img)
cv2.waitKey()