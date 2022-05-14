import cv2 as cv
from cv2 import bitwise_and
from cv2 import bitwise_or
from cv2 import bitwise_not
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('BLANK',blank)
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('CIRCLE',circle)
cv.imshow('RECT',rectangle)

#and-common region(intersecting region)
bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow('BITwise AND',bitwise_and)


#or(non intersecting region and intersecting region)
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow('BITwise OR',bitwise_or)

#bitwise exor(non intersecting)
bitwise_exor=cv.bitwise_xor(rectangle,circle)
cv.imshow('BITwise EXOR',bitwise_exor)

#not-converts black part to white and white part to black
bitwise_not=cv.bitwise_not(rectangle)
cv.imshow('BITwise NOT',bitwise_not)

cv.waitKey(0)