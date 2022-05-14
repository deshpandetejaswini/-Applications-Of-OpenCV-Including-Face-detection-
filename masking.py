import cv2 as cv
import numpy as np
img= cv.imread('PHOTOS/cats.jpg')
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('cat',img)
blank=np.zeros(img.shape[:2],dtype='uint8')

cv.imshow('BLANK',blank)
cv.waitKey (0)

mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('mask',mask)
cv.waitKey (0)


masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('masked',masked)
cv.waitKey (0)




grmasked=cv.bitwise_and(grey,grey,mask=mask)
cv.imshow('grmasked',grmasked)
cv.waitKey (0)

