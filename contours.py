import cv2 as cv
import numpy as np
img= cv.imread('PHOTOS/cat27.4.jpg')
cv.imshow('cat',img)
cv.waitKey(0)


grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('catwg',grey)
cv.waitKey(0)


blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('BLANK',blank)
cv.waitKey(0)

#blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
cv.waitKey(0)


#edges
canny=cv.Canny(blur,125,175)
cv.imshow('Canny',canny)
cv.waitKey(0)



#thresholding image-binaraising image
ret,thresh=cv.threshold(grey,125,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)
cv.waitKey(0)



#counting edges
contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
cv.waitKey(0)



#copying contours on blank images -foe this we compulsoryly require
#counting edges writen above
cv.drawContours(blank,contours,-1,(0,0,225),thickness=1)
cv.imshow('red',blank)
cv.waitKey(0)