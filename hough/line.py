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

img = cv2.imread('../src/sudoku.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize = 3)

lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img, (x1,y1), (x2,y2), (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow('Bordas da Imagem Canny', edges)
cv2.imshow('Detector de Linhas', img)
cv2.waitKey()