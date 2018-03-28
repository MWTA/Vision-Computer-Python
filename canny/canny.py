#coding: utf-8
#!/usr/bin/python
# <https://programarfacil.com/blog/vision-artificial/detector-de-bordes-canny-opencv/>

import numpy as np
import cv2
 
# Carrega a imagem e exibe em uma janela.
img_orig = cv2.imread("../src/35008.jpg")
cv2.imshow("Imagem img_orig", img_orig)
 
# Converte a imagem para escala de cinza.
gray = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
 
# Aplica suavização Gaussiano (filtragem da imagem para eliminar o ruído) e exibe em uma janela
gauss = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("Gaussian", gauss)
 
# Detecta as bordas com Canny e exibe na tela.
canny = cv2.Canny(gauss, 50, 150)
cv2.imshow("Deteccao de Bordas - Canny", canny)
 
# Procura por contorno dentro de bordas detectadas.
(_, contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
# Mostra o numero de objetos encontrados.
print("Foi encontrado {} objetos".format(len(contornos)))

# Desenha os contonos encontrado e mostra em uma janela 
cv2.drawContours(img_orig, contornos, -1, (0, 0, 255), 1)
cv2.imshow("Desenha Contornos", img_orig)
 
cv2.waitKey(0)