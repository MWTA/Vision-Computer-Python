#coding: utf-8
#!/usr/bin/python

'''
REFERÊNCIAS:
	<http://acodigo.blogspot.com.br/2017/08/deteccion-de-contornos-con-opencv-python.html>

@Author RodriguesFAS
@Date 26/09/2017
@Email <fasr@cin.ufpe.br> || <franciscosouzaacer@gmail.com>
@site <htpp://rodriguesfas.com.br>

'''

# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np

img_org = cv2.imread('../src/herramientas.jpg')

gray = cv2.cvtColor(img_org, cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray, (7, 7), 3)

t, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)

# obtendo os contornos
_, contours, _ = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# desenha os contornos
cv2.drawContours(img_org, contours, -1, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('Limiar', dst)
cv2.imshow('Desenha Contornos', img_org)

# Limitando onde desenhar os contornos
for c in contours:
    area = cv2.contourArea(c)
    if area > 1000 and area < 10000:
        cv2.drawContours(img_org, [c], 0, (0, 255, 0), 2, cv2.LINE_AA)
    	cv2.imshow('Limitar onde desenhar contornos', img_org)

# obtendo retangulos
for c in contours:
    area = cv2.contourArea(c)
    if area > 1000 and area < 10000:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img_org, (x, y), (x + w, y + h), (0, 255, 0), 1, cv2.LINE_AA)
        cv2.imshow('Desenha retangulos nos contornos', img_org)

cv2.waitKey(0)