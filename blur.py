import cv2 as cv
import numpy as np
img= cv.imread('PHOTOS/cat27.4.jpg')
cv.imshow('cat',img)
#median blur
median=cv.medianBlur(img,3)
cv.imshow('Mediamblur',median)
cv.waitKey(0)
#avg blur
avg=cv.blur(img,(7,7),0)
cv.imshow('average',avg)
cv.waitKey(0)
#gauss blur
gauss=cv.GaussianBlur(img,(7,7),0)
cv.imshow('gaussian blur',gauss)
cv.waitKey(0)
#bilateral blur
blt=cv.bilateralFilter(img,5,15,15)
cv.imshow('bilateral blur',blt)
cv.waitKey(0)
