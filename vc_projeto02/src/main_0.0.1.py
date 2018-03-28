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
from matplotlib import pyplot as plt
from scipy import signal
import time



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



# illustrated output img (Secion 2.3 Article)
def illustrated(img):
    return img



# Input image - 
def inputImg():
    img = cv2.imread('../src/img/input/02.jpg', 0)
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
    img = cv2.equalizeHist(img)
    cv2.imshow('Step 01 - Image Enhancement (Equalize Histogram)', img)
    #outHist(img)
    return img



'''
Step 02 - Median Filtering (LPF)
 
Devido ao passo anterior, é obvio que o número de pontos de contorno do rosto, podem almentar,
o que significa, que a informação facial foi fortalecida. O ruído também foi aprimorado. 
Por meio da filtragem, podem ser apagados as fontes de ruídos presente na imagem, aplicando um
filtro de passa mediana.
'''
def step_02(img):
    # Median Blurring
    img = cv2.medianBlur(img, 5)
    cv2.imshow('Step 02 - Median Filtering', img)
    #outHist(img)
    return img



'''
Step 03 - Edge Detection

Existe muitos detectores de bordas, considerando o custo computacional e o desempenho foi usado
o zero-crossing detector: Difference of Exponential (DoE).
'''
def step_03(img):

    # converte a imagem para uma matriz de pixels.
    pixels = np.array(img, dtype=float)

    # Convolução por Diferenciação de kernel Gaussiano
    DoGkernel = np.array(([
        [ 0,  0, -1, -1, -1,  0,  0],
        [ 0, -2, -3, -3, -3, -2,  0],
        [-1, -3,  5,  5,  5, -3, -1],
        [-1, -3,  5, 24,  5, -3, -1],
        [-1, -3,  5,  5,  5, -3, -1],
        [ 0, -2, -3, -3, -3, -2,  0],
        [ 0,  0, -1, -1, -1,  0,  0]
        ]), 
    np.float32)

    DoGkernel= np.flipud(np.fliplr(DoGkernel))

    DoGImage = signal.convolve2d(pixels, DoGkernel, mode='full', boundary='fill', fillvalue=0)

    DoGzcross = np.ones((len(DoGImage), len(DoGImage[0])))
    DoGzcross2 = np.ones((len(DoGImage), len(DoGImage[0])))

    # Finding Zero Crossing
    for i in range(len(DoGImage) - 1):
        for j in range(len(DoGImage[0]) - 1):
            count = 0
            lst = []
            lst.append(DoGImage[i][j])
            lst.append(DoGImage[i+1][j])
            lst.append(DoGImage[i+1][j+1])
            lst.append(DoGImage[i][j+1])
            
            if DoGImage[i][j] < 0: count = count + 1
            if DoGImage[i+1][j] < 0: count = count + 1
            if DoGImage[i+1][j+1] < 0: count = count + 1
            if DoGImage[i][j+1] < 0: count = count + 1

            if count > 0 & count < 4: 
                DoGzcross[i][j] = 0
                
                #### thresholding zero-crossing ####
                if max(lst) - min(lst) >= 400: DoGzcross2[i][j] = 0

    cv2.imshow('Step 03 - Edge Detection (DoG Z-Crossing)', DoGzcross)

    return DoGzcross



# Step 04 - Edge Linking
def step_04(img):
    minLineLength=100

    #lines = cv2.HoughLinesP(image=img,rho=1,theta=np.pi/180, threshold=100,lines=np.array([]), minLineLength=minLineLength,maxLineGap=80)

    cv2.imshow('Step 04 - Edge Linking', img)
    
    return img



# Step 05 - Template Matching
#def step_05(img):
    #cv2.imshow('Step 05 - Template Matching', img)
    #return img



# Exit
def exit():
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Main
def main():
    start_time = time.time()

    img_orig = inputImg()
    img_hist = step_01(img_orig)
    img_blur = step_02(img_hist)
    img_edge = step_03(img_blur)
    img_link = step_04(img_edge)
    #step_05(img_link)

    end_time = time.time()
    time_taken = end_time - start_time

    print "Time taken for execution: ", time_taken

    exit()



# Main
if __name__ == "__main__": main()