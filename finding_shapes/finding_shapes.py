#coding: utf-8
#!/usr/bin/python

'''
@Author RodriguesFAS
@Date 06/09/2017
@Email <fasr@cin.ufpe.br> || <franciscosouzaacer@gmail.com>
@site <htpp://rodriguesfas.com.br>
'''

# import the necessary packages
import numpy as np
import argparse
import cv2
 
# load the image
image = cv2.imread('../src/shapes.png')

# find all the 'black' shapes in the image
lower = np.array([0, 0, 0])
upper = np.array([15, 15, 15])
shapeMask = cv2.inRange(image, lower, upper)

# find the contours in the mask
(_, cnts, _) = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print "I found %d black shapes" % (len(cnts))
cv2.imshow("Mask", shapeMask)

# loop over the contours
for c in cnts:
	# draw the contour and show it
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.imshow("Image", image)
	cv2.waitKey(0)

cv2.imshow('Shape Mask', shapeMask)
cv2.waitKey(0)