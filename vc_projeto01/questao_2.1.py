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

img_orig = cv2.imread("../src/35008.jpg")
cv2.imshow("Imagem img_orig", img_orig)
 
gray = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagem escala de cinza", gray)
 
gauss = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("Filtro Gaussian", gauss)
 
canny = cv2.Canny(gauss, 50, 150)
cv2.imshow("Deteccao de Bordas - Canny", canny)
 
(_, contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
print("Foi encontrado {} objetos".format(len(contornos)))

cv2.drawContours(img_orig, contornos,-1,(0, 0, 255), 1)
cv2.imshow("Desenha Contornos", img_orig)
 
cv2.waitKey(0)
