#coding: utf-8
#!/usr/bin/python
# Python 2/3 compatibility

'''

@ Article Title: A new face detection method based on shape information
@ Article Url: <http://www.sciencedirect.com/science/article/pii/S0167865500000088>
@ Article Implemented by Francisco de Assis de Souza Rodrigues - RodriguesFAS
@ Date 21/10/2017
@ Email <fasr@cin.ufpe.br> || <franciscosouzaacer@gmail.com>
@ Website <htpp://rodriguesfas.com.br>

@ References
    DOC, OpenCV. Histogram Equalization. Disponível em: <https://docs.opencv.org/3.1.0/d5/daf/tutorial_py_histogram_equalization.html>. Acesso 21/10/2017.
    DOC, OpenCV. Smoothing Images. Disponível em: <https://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html>. Acesso 21/10/2017.
    HIPR2. Zero Crossing Detector. Disponível em: <https://homepages.inf.ed.ac.uk/rbf/HIPR2/zeros.htm>. Acesso 30/10/2017.
    HONG. IMAGE EDGE DETECTION : SOBEL AND LAPLACIAN. Disponível em: <http://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Gradient_Sobel_Laplacian_Derivatives_Edge_Detection.php>. Acesso 2181082017.

'''



# Import lib's.
import cv2
import numpy as np
import numpy
from matplotlib import pyplot as plt
from scipy import signal
import time
import scipy.ndimage as ndi
import scipy
import Image
import math
from math import pi



img_orig = "../src/img/01.jpg"

img = Image.open(img_orig)

width = img.size[1]
height = img.size[0]

gnh = numpy.zeros((width, height))
gnl = numpy.zeros((width, height))

sigma = 2.2



# outHist - Exibe resultado do histograma da imagem em questão.
def outHist(img):

    hist, bins = np.histogram(img.flatten(), 256, [0,256])

    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max()/ cdf.max()

    plt.plot(cdf_normalized, color = 'b')
    plt.hist(img.flatten(), 256, [0,256], color = 'r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc = 'upper left')
    plt.show()



# Input image - 
def inputImg():
    img = cv2.imread(img_orig, 0)
    cv2.imshow('Image Original', img)
    #outHist(img)
    return img



'''
Step 01 - Image Enhancement

As imagens de entrada, podem ter um contraste muito fraco devido à limitação das condições
de iluminação. Nesse passo, a equalização do histograma é usada para melhorar o contraste 
da imagem original.
'''
def step_01(img):
    img_hist = cv2.equalizeHist(img)
    scipy.misc.imsave('img_hist.jpg', img_hist)
    cv2.imshow('Step 01 - Image Enhancement (Equalize Histogram)', img_hist)
    #outHist(img)
    return img_hist



'''
Step 02 - Median Filtering (LPF)
 
Devido ao passo anterior, é obvio que o número de pontos de contorno do rosto, podem almentar,
o que significa, que a informação facial foi fortalecida. O ruído também foi aprimorado. 
Por meio da filtragem, podem ser apagados as fontes de ruídos presente na imagem, aplicando um
filtro de passa mediana.
'''
def step_02(img):
    # Median Blurring
    img_blur = cv2.medianBlur(img, 5)
    scipy.misc.imsave('img_blur.jpg', img_blur)
    cv2.imshow('Step 02 - Median Filtering', img_blur)
    #outHist(img)
    return img_blur



'''
Step 03 - Edge Detection

Existe muitos detectores de bordas, considerando o custo computacional e o desempenho foi usado
o zero-crossing detector: Difference of Exponential (DoE).
'''
def step_03():
    img = Image.open("img_blur.jpg").convert('L')
    
    img_pixels = np.array(img, dtype=float)
    
    G = ndi.filters.gaussian_filter(img_pixels, sigma)
    
    sobelout = Image.new('L', img.size)

    gradx = np.array(sobelout, dtype=float)
    grady = np.array(sobelout, dtype=float)

    sobel_x = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
        ]

    sobel_y = [
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
        ]

    #calculate |G| and dir(G)
    for x in range(1, width-1):
        for y in range(1, height-1):
            px = (sobel_x[0][0] * G[x-1][y-1]) + (sobel_x[0][1] * G[x][y-1]) + \
                 (sobel_x[0][2] * G[x+1][y-1]) + (sobel_x[1][0] * G[x-1][y]) + \
                 (sobel_x[1][1] * G[x][y]) + (sobel_x[1][2] * G[x+1][y]) + \
                 (sobel_x[2][0] * G[x-1][y+1]) + (sobel_x[2][1] * G[x][y+1]) + \
                 (sobel_x[2][2] * G[x+1][y+1])

            py = (sobel_y[0][0] * G[x-1][y-1]) + (sobel_y[0][1] * G[x][y-1]) + \
                 (sobel_y[0][2] * G[x+1][y-1]) + (sobel_y[1][0] * G[x-1][y]) + \
                 (sobel_y[1][1] * G[x][y]) + (sobel_y[1][2] * G[x+1][y]) + \
                 (sobel_y[2][0] * G[x-1][y+1]) + (sobel_y[2][1] * G[x][y+1]) + \
                 (sobel_y[2][2] * G[x+1][y+1])

            gradx[x][y] = px
            grady[x][y] = py

    sobeloutmag = scipy.hypot(gradx, grady)
    sobeloutdir = scipy.arctan2(grady, gradx)

    scipy.misc.imsave('cannynewmag.jpg', sobeloutmag)
    scipy.misc.imsave('cannynewdir.jpg', sobeloutdir)

    for x in range(width):
        for y in range(height):
            if (sobeloutdir[x][y]<22.5 and sobeloutdir[x][y]>=0) or \
                (sobeloutdir[x][y]>=157.5 and sobeloutdir[x][y]<202.5) or \
                (sobeloutdir[x][y]>=337.5 and sobeloutdir[x][y]<=360):
                sobeloutdir[x][y]=0
            elif (sobeloutdir[x][y]>=22.5 and sobeloutdir[x][y]<67.5) or \
                (sobeloutdir[x][y]>=202.5 and sobeloutdir[x][y]<247.5):
                sobeloutdir[x][y]=45
            elif (sobeloutdir[x][y]>=67.5 and sobeloutdir[x][y]<112.5)or \
                (sobeloutdir[x][y]>=247.5 and sobeloutdir[x][y]<292.5):
                sobeloutdir[x][y]=90
            else:
                sobeloutdir[x][y]=135


    scipy.misc.imsave('cannynewdirquantize.jpg', sobeloutdir)

    mag_sup = sobeloutmag.copy()

    for x in range(1, width-1):
        for y in range(1, height-1):
            if sobeloutdir[x][y]==0:
                if (sobeloutmag[x][y]<=sobeloutmag[x][y+1]) or \
                    (sobeloutmag[x][y]<=sobeloutmag[x][y-1]):
                    mag_sup[x][y]=0
            elif sobeloutdir[x][y]==45:
                if (sobeloutmag[x][y]<=sobeloutmag[x-1][y+1]) or \
                    (sobeloutmag[x][y]<=sobeloutmag[x+1][y-1]):
                    mag_sup[x][y]=0
            elif sobeloutdir[x][y]==90:
                if (sobeloutmag[x][y]<=sobeloutmag[x+1][y]) or \
                    (sobeloutmag[x][y]<=sobeloutmag[x-1][y]):
                    mag_sup[x][y]=0
            else:
                if (sobeloutmag[x][y]<=sobeloutmag[x+1][y+1]) or \
                    (sobeloutmag[x][y]<=sobeloutmag[x-1][y-1]):
                    mag_sup[x][y]=0

    scipy.misc.imsave('cannynewmagsup.jpg', mag_sup)

    m = numpy.max(mag_sup)
    th = 0.2*m
    tl = 0.1*m


    gnh = numpy.zeros((width, height))
    gnl = numpy.zeros((width, height))

    for x in range(width):
        for y in range(height):
            if mag_sup[x][y]>=th:
                gnh[x][y]=mag_sup[x][y]
            if mag_sup[x][y]>=tl:
                gnl[x][y]=mag_sup[x][y]

    scipy.misc.imsave('cannynewgnlbeforeminus.jpg', gnl)
    gnl = gnl-gnh
    scipy.misc.imsave('cannynewgnlafterminus.jpg', gnl)
    scipy.misc.imsave('cannynewgnh.jpg', gnh)

    for i in range(1, width-1):
        for j in range(1, height-1):
            if gnh[i][j]:
                gnh[i][j]=1
                traverse(i, j)

    scipy.misc.imsave('cannynewout.jpg', gnh)

    #cv2.imshow('Step 03 - Edge Detection (DoG Z-Crossing)', DoGzcross)

    #return DoGzcross



def traverse(i, j):
    x = [-1, 0, 1, -1, 1, -1, 0, 1]
    y = [-1, -1, -1, 0, 0, 1, 1, 1]
    
    for k in range(8):
        if gnh[i+x[k]][j+y[k]]==0 and gnl[i+x[k]][j+y[k]]!=0:
            gnh[i+x[k]][j+y[k]]=1
            traverse(i+x[k], j+y[k])



# Step 04 - Edge Linking
def step_04(img):

    cv2.imshow('Step 04 - Edge Linking', img)
    
    return img



# Step 05 - Template Matching
def step_05(img):

    cv2.imshow('Step 05 - Template Matching', img)
    #return img



# Exit
def exit():
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Main
def main():
    start_time = time.time()

    img_start = inputImg()
    img_hist = step_01(img_start)
    img_blur = step_02(img_hist)
    img_edge = step_03()
    #img_link = step_04(img_edge)
    #step_05(img_link)

    end_time = time.time()
    time_taken = end_time - start_time

    print "Time taken for execution: ", time_taken

    exit()



# Main
if __name__ == "__main__": main()