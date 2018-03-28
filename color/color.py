#coding: utf-8
#!/usr/bin/python

'''
@Author RodriguesFAS
@Date 07/09/2017
@Email <fasr@cin.ufpe.br> || <franciscosouzaacer@gmail.com>
@site <htpp://rodriguesfas.com.br>
'''

# Python 2/3 compatibility
from __future__ import print_function
import  cv2        #disponibiza as funções do opencv
import numpy as np
 
 
def filtroRGB(src,r,g,b):
    if r == 0:
        src[:,:,2] = 0    #elimina o vermelho
    if g == 0:
        src[:,:,1] = 0    #elimina o verde
    if b == 0:
        src[:,:,0] = 0    #elimina o azul
 
def show_image():
    filtro=1
 
    while True:
        img = cv2.imread("../src/folha.jpg")
 
        if filtro == 1:
            cv2.imshow('Estudo OpenCV- Filtro', img)
 
        if filtro == 2:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Estudo OpenCV- Filtro',gray)
 
 
        if filtro == 6:
            filtroRGB(img,1,0,0)
            cv2.imshow('Estudo OpenCV- Filtro', img)
 
 
        if filtro == 7:
            filtroRGB(img,0,1,0)
            cv2.imshow('Estudo OpenCV- Filtro', img)
 
        if filtro == 8:
            filtroRGB(img,0,0,1)
            cv2.imshow('Estudo OpenCV- Filtro',img)
 
        ret= cv2.waitKey(1)
 
        if ret==27:
            break
 
        elif ret==-1:
           continue
 
        elif ret== 49:
           filtro= 1
 
        elif ret== 50:
           filtro= 2
 
        elif ret== 54:
           filtro= 6
 
        elif ret== 55:
          filtro= 7
 
        elif ret== 56:
          filtro= 8
 
cv2.destroyAllWindows()
 
 
def main():
    show_image()
    return 0
 
if __name__ == '__main__':
    main()