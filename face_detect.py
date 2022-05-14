import cv2 as cv
import numpy as np
img= cv.imread('PHOTOS/group 1.jpg')
cv.imshow('lady',img)
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('greylady',gray)
haar_cascade=cv.CascadeClassifier('har_face.xml')
faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1)#keep minneb big number so that it detects correct no of faces
#returns rectangular coordinates of face as a list to faces_rect
print("no of people in the image are")
print(len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('detected faces',img)    
cv.waitKey(0)



#############################3
""" capture=cv.VideoCapture(0)
while True :
    isTrue, frame=capture.read()
    haar_cascade=cv.CascadeClassifier('har_face.xml')
    faces_rect1=haar_cascade.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=1)
    for (x,y,w,h) in faces_rect1:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

    cv.imshow('video',frame)

    if cv.waitKey(10) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()



 """
# Loading the cascades vedio part
face_cascade = cv.CascadeClassifier('har_face.xml')


# Defining a function that will do the detections
def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
    
        
    return frame

# Doing some Face Recognition with the webcam
video_capture = cv.VideoCapture(0)
while True:
    _, frame = video_capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv.imshow('Video', canvas)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv.destroyAllWindows()









cv.waitKey(0)