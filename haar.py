## Haar cascades .xml files:
#https://github.com/opencv/opencv/tree/master/data/haarcascades
import numpy as np
import cv2

## Import the face cascade classifier
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

## Import the face cascade classifier
eyes_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")

## Start video capture with the camera
# The argument may be changed for
# a path with a video
cap=cv2.VideoCapture(0)

## Infinite loop
while True:
    ## Reading the capture and writing the frame
    _,img=cap.read()

    ## Converting image to grayscale
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ## Will search for faces on the grayscale frame
    faces=face_cascade.detectMultiScale(gray, 1.3, 5)

    ## For each face encountered, a rectangle will be drown
    # around it and a roi (region of interest) will be defined 
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]

        ## Will search for eyes in the given roi
        eyes=eyes_cascade.detectMultiScale(roi_gray)

        ## For each eye found, draw a rectangle around it
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
    
    ## Show the result
    cv2.imshow("Result",img)

    ## If 'q' key is pressed, exit loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

## Release the capture and closes 
# all windows
cap.release()
cv2.destroyAllWindows()