#thresholding means binarising the image 
#2 parameters thresh means the binarised image and threshhold means 150
import cv2 as cv
import numpy as np
img= cv.imread('PHOTOS/cats.jpg')
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('cat',img)
cv.imshow('grey',grey)
threshold,thresh=cv.threshold(grey,150,255,cv.THRESH_BINARY)
#pixels intensities greater than 150 are set to 255(white) and less than  150 are set to 0(black)
cv.imshow('simple thresh',thresh)



#inverse threshold value
threshold,thresh_inv=cv.threshold(grey,150,255,cv.THRESH_BINARY_INV)
#pixels intensities lesser than 150 are set to 255(white) and greater than  150 are set to 0(black)
cv.imshow('inverse thresh',thresh_inv)








#adaptive thresh (finds out thresh by itself )-cernel size /block size used for
# finging average value of thresh for the sorrounding blocks
adaptive_thresh =cv.adaptiveThreshold(grey,225,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('adaptive thresh',adaptive_thresh)

#inverse adp threshold
adaptive_thresh =cv.adaptiveThreshold(grey,225,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,3)
cv.imshow('adaptive inv thresh',adaptive_thresh)



cv.waitKey(0)