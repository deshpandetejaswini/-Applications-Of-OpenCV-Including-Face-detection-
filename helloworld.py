import cv2 as cv
img= cv.imread('PHOTOS/cat27.4.jpg')
cv.imshow('cat',img)




def rescale_frame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimentions=(width,height)
    return cv.resize(frame,dimentions,interpolation=cv.INTER_AREA)
ans=rescale_frame(img)
cv.imshow("resize",ans)













capture=cv.VideoCapture(0)
while True :
    isTrue, frame=capture.read()
    new_frame=rescale_frame(frame,scale=.26)
    cv.imshow('video',frame)
    cv.imshow('VVVV',new_frame)
    if cv.waitKey(10) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

