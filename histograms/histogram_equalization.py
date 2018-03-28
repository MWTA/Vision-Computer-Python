#coding: utf-8
#!/usr/bin/python
# Python 2/3 compatibility

'''
Histograms - 2: Histogram Equalization
<https://docs.opencv.org/3.1.0/d5/daf/tutorial_py_histogram_equalization.html>
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../src/histeq_numpy1.jpg', 0)

hist, bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

