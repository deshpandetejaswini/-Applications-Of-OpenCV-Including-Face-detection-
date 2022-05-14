import cv2 as cv
import numpy as np
#we can convert bgr to other forms
#we can convert other forms to bgr
#but you cannot convert hsv to greyscele directly
#colorspace1-->bgr-->colorspace2
#opencv displays bgr image
img= cv.imread('PHOTOS/cat27.4.jpg')
cv.imshow('cat',img)
cv.waitKey(0)


grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grey',grey)
cv.waitKey(0)
#bgrtohsv
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)
cv.waitKey(0)
#bgrtolab
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)
cv.waitKey(0)
#bgrtorgb
iv=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',iv)
cv.waitKey(0)






#hsvtobgr
hsv_to_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSVTOBGR',hsv_to_bgr)
cv.waitKey(0)

 