#coding: utf-8
#!/usr/bin/python

'''
@Author RodriguesFAS
@Date 04/10/2017
@Email <fasr@cin.ufpe.br> || <franciscosouzaacer@gmail.com>
@site <htpp://rodriguesfas.com.br>
<http://acodigo.blogspot.com.br/2017/06/manipular-pixeles-opencv-python.html>
'''

# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np

img_base = cv2.imread('../src/parafuso_porca.bmp')
#cv2.imshow('Img Base', img_base)

img_alvo = cv2.imread('../src/objetos.bmp')
#cv2.imshow('Img Alvo', img_alvo)

img_gray_base = cv2.cvtColor(img_base, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Img Gray', img_gray_base)

img_gray_obj = cv2.cvtColor(img_alvo, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Img Gray', img_gray_obj)

template_porca = img_gray_base[275:390, 70:170]
#cv2.imshow('Template Porca', template_porca)

template_parafuso = img_gray_base[30:510, 205:335]
cv2.imshow('Template Parafuso', template_parafuso)

wPor, hPor = template_porca.shape[::-1]
wPar, hPar = template_parafuso.shape[::-1]

resPor = cv2.matchTemplate(img_gray_obj, template_porca, cv2.TM_CCOEFF_NORMED)
thresholdPor = 0.8
loc_Por = np.where(resPor >= thresholdPor)

resPar = cv2.matchTemplate(img_gray_obj, template_parafuso, cv2.TM_CCOEFF_NORMED)
thresholdPar = 0.7
loc_Par = np.where(resPar >= thresholdPar)

porca = 0
parafuso = 0

for ptPor in zip(*loc_Por[::-1]):
    cv2.rectangle(img_alvo, ptPor, (ptPor[0] + wPor, ptPor[1] + hPor), (0, 255, 0), 1)
    porca+=1

for ptPar in zip(*loc_Par[::-1]):
    cv2.rectangle(img_alvo, ptPar, (ptPar[0] + wPar, ptPar[0] + hPar), (0, 255, 0), 1)
    parafuso+=1

cv2.imshow('Objetos Detectados', img_alvo)

#print("Encontrado {0} parafuso(s).".format(parafuso))
#print("Encontrado {0} porca(s)".format(porca))

cv2.waitKey(0)
cv2.destroyAllWindows()