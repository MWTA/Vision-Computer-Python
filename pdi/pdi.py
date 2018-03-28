#coding: utf-8
#!/usr/bin/python

'''
REFERÊNCIAS:
	<http://acodigo.blogspot.com.br/2013/05/procesamiento-de-imagenes-en-opencv.html>

@Author RodriguesFAS
@Date 26/09/2017
@Email <fasr@cin.ufpe.br> || <franciscosouzaacer@gmail.com>
@site <htpp://rodriguesfas.com.br>

'''

# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np

src = 'src/lena.jpg'

img_org = cv2.imread(src)

t, dst1 = cv2.GaussianBlur(img, dst, Size(13,7), 8)

cv2.imshow('GaussianBlur', dst1)

cv2.waitKey(0)