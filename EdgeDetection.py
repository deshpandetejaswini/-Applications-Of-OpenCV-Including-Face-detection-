
from cgitb import grey
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('Photos/cats.jpg')



cv.imshow('catf',img)
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grey',grey)
#grayscale imageyhist




canny=cv.Canny(grey,125,175)
cv.imshow('Canny',canny)
cv.waitKey(0)

#laplacian
lap=cv.Laplacian(grey,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)
cv.waitKey(0)
#sobel
sobelx=cv.Sobel(grey,cv.CV_64F,1,0)
sobely=cv.Sobel(grey,cv.CV_64F,1,0)
combi=cv.bitwise_or(sobelx,sobely)
cv.imshow('Sobelx',sobelx)
cv.imshow('sobely',sobely)
cv.imshow('combi',combi)











cv.waitKey(0)