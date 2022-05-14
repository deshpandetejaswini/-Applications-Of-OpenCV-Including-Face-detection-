import cv2 as cv
import numpy as np
img= cv.imread('PHOTOS/cat27.4.jpg')
cv.imshow('cat',img)


def trans(img,x,y):
    #moving up down left right
    transmat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimensions)
transl=trans(img,100,100)
cv.imshow('translated',transl)
cv.waitKey(0)
#rotate the image
def rotate(img,angle,rotPoint=None):
        (height,width)=img.shape[:2]
        
        if rotPoint is None:
            rotPoint=(width//2,height//2)
        rotmat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
        dimension=(width,height)
        return cv.warpAffine(img,rotmat,dimension)
rotated=rotate(img,45)
cv.imshow('ro',rotated)
cv.waitKey(0)
#resize the image 
re= cv.resize(img,[500,500],interpolation=cv.INTER_CUBIC)
cv.imshow('resize',re)
cv.waitKey(0)


#flipping
fli=cv.flip(img,1)#0-invert,1,-1 flip code to rotate
cv.imshow('flip',fli)
cv.waitKey(0)
 #cropping
C=img[200:400,300:400]
cv.imshow('cropping',C)
cv.waitKey(0)     
              
            
    