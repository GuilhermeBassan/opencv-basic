import cv2

## Start video capture with the camera
# The argument may be changed for
# a path with a video
cap = cv2.VideoCapture(0)

## Infinite loop
while True:
    ## Read frame from the capture
    ret, frame = cap.read()

    ## Show read frame
    cv2.imshow("Frame", frame)

    ## If 'q' key is pressed, exit loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

## Release the capture and closes 
# all windows
cap.release()
cv2.destroyAllWindows()
