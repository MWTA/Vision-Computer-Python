
#coding: utf-8
#!/usr/bin/python
'''
This is the classical Hough transform as described in wikipedia. 
The code does not compute averages; it merely makes a point on 
the transformed image darker if a lot of points on the original 
image lie on the corresponding line. The output is almost identical 
to that of the Tcl code. The code works only with gray-scale images, 
but it is easy to extend to RGB.

<https://rosettacode.org/wiki/Hough_transform#Python>

13/10/2017
'''

from math import hypot, pi, cos, sin
from PIL import Image
 
 
def hough(im, ntx=460, mry=360):
    "Calculate Hough transform."
    pim = im.load()
    nimx, mimy = im.size
    mry = int(mry/2)*2          #Make sure that this is even
    him = Image.new("L", (ntx, mry), 255)
    phim = him.load()
 
    rmax = hypot(nimx, mimy)
    dr = rmax / (mry/2)
    dth = pi / ntx
 
    for jx in xrange(nimx):
        for iy in xrange(mimy):
            col = pim[jx, iy]
            if col == 255: continue
            for jtx in xrange(ntx):
                th = dth * jtx
                r = jx*cos(th) + iy*sin(th)
                iry = mry/2 + int(r/dr+0.5)
                phim[jtx, iry] -= 1
    return him
 
 
def test():
    "Test Hough transform with pentagon."
    im = Image.open("../src/pentagono.png").convert("L")
    him = hough(im)
    him.save("pentagono.bmp")
 
 
if __name__ == "__main__": test()