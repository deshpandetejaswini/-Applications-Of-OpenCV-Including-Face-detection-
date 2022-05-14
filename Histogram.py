#histogram allow to analize pixel intensities

from cgitb import grey
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('Photos/cats.jpg')



cv.imshow('catf',img)
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('grey',grey)
cv.waitKey(0)

#grayscale imageyhist
grey_hist=cv.calcHist([grey],[0],None,[256],[0,256])
plt.figure()
plt.title('greyhistogram')
plt.xlabel('bins')#bins means intervals of pixle intensities
plt.ylabel('no of pixles')
plt.plot(grey_hist)
plt.xlim([0,256])
plt.show()
cv.waitKey(0)
#masking process
blank=np.zeros(img.shape[:2],dtype='uint8')
mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
masked=cv.bitwise_and(grey,grey,mask=mask)
#colmasked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('masked',masked)
#cv.imshow('masked',colmasked)
cv.waitKey (0)






########################################




 #histogram for masked imagey
maskhist=cv.calcHist([masked],[0],masked,[256],[0,256])
plt.figure()
plt.title('maskedhistogram')
plt.xlabel('bins for masked histogram')#bins means intervals of pixle intensities
plt.ylabel('no of pixles')
plt.plot(maskhist)
plt.xlim([0,256])
plt.show()
cv.waitKey(0)


#ccolor histogram for image
plt.figure()
plt.title('coloreddhistogram')
plt.xlabel('bins for histogram')#bins means intervals of pixle intensities
plt.ylabel('no of pixles')




colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
    


plt.show()
cv.waitKey(0)


#histogram for masked images
plt.figure()
plt.title('coloreddhistogramformaskedimag')
plt.xlabel('bins for masked histogram')#bins means intervals of pixle intensities
plt.ylabel('no of pixles')

colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],masked,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
    


plt.show()





    

 
 






cv.waitKey(0)