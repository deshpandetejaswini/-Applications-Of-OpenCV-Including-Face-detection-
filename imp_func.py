import cv2 as cv
#import matplotlib.pyplot as plt
#opencv follows bgr formatting
#convert to black and white
#outside opencv rgb is used
img=cv.imread('PHOTOS/cat27.4.jpg')
cv.imshow('catr',img)
cv.waitKey(0)
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grey',grey)
cv.waitKey(0)
#blur a image 
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
cv.waitKey(0)
#edges
canny=cv.Canny(blur,125,175)
cv.imshow('Canny',canny)
cv.waitKey(0)

