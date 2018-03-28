#coding: utf-8
#!/usr/bin/python

'''
@Author RodriguesFAS
@Date 29/09/2017
@Email <fasr@cin.ufpe.br> || <franciscosouzaacer@gmail.com>
@site <htpp://rodriguesfas.com.br>
'''

import cv2
import numpy as np

# read sample images
img1 = cv2.imread("../src/ESTEIRA0-300x225.jpg")
img2 = cv2.imread("../src/ESTEIRA1-300x225.jpg")
img3 = cv2.imread("../src/mask-300x225.jpg")

# convert the images for gray scale
imgray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
imgray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
imgray3 = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)

# kernel to use for erode imagem
kernel = np.ones((2, 2), np.uint8)

#find the diference betwen img1 and img2
diference = cv2.subtract(imgray1, imgray2)

# turn white all pixels non-zero (binary image)
diference[diference > 0] = 255

# erode to erase the noise
erode1 = cv2.erode(imgray3, kernel, iterations = 2)
erode = cv2.erode(diference, kernel, iterations = 2)
cv2.imshow('MASK', erode)

# says if the image contain any pixel non-zero
result = np.any(diference)

#read the counter sample to compare
im1, cont1, hier1 = cv2.findContours(erode1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

#find contours
im2, cont, hier = cv2.findContours(erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

fruits = [0, 0, 0]

for i in range(0, len(cont)):
	result = [0, 0]
	for j in range(0, len(cont1)):
		result[j] = cv2.matchShapes(cont1[j], cont[i], 1, 0)
		index = result.index(min(result))
		
		if index is 0:
			fruits[i] = "banana"
			print(min(result))
		else:
			fruits[i] = "laranja"
			print(min(result))
			fruits = np.array(fruits)

# draw the rectangle of the contour
if len(cont) > 0:
	num = 0
	for c in cont:
		x, y, w, h = cv2.boundingRect(c)
		cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img2, fruits[num],(x, y-10), font, 0.8,(0, 255, 0), 2, cv2.LINE_AA)
		num += 1

# show the result
if result is not True:
	print("As imagens nao sao iguais")
	cv2.imshow('DETECCAO', img2)
	cv2.waitKey(0)
else:
	print("As imagens sao iguais")