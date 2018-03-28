#coding: utf-8
#!/usr/bin/python
# Python 2/3 compatibility

# Import lib's.
import cv2
import glob

filenames = [img for img in glob.glob("../src/*.jpg")]

filenames.sort() # ADD THIS LINE

images = []
for img in filenames:
    n= cv2.imread(img)
    images.append(n)
    print (img)