import cv2 as cv
import numpy as np
#paint image by color
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('BLANK',blank)
#blank[200:300,300:400]=255,0,0
#cv.imshow('NEW',blank)
#cv.waitKey (0)
#rectangle
cv.rectangle(blank,(0,0),(250,500),(0,255,0),thickness=-1)
cv.imshow('rect',blank)
cv.waitKey (0)
#circle
cv.circle(blank,(250,250),24,(250,0,0),thickness=-1)
cv.imshow('circle',blank)
cv.waitKey (0)
#line
cv.line(blank,(0,0),(250,250),(250,250,250),thickness=3)
cv.imshow('line',blank)
cv.waitKey (0)
#text
cv.putText(blank,'Hello',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,0,0),thickness=2)
cv.imshow('text',blank)
cv.waitKey (0)