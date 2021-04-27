import cv2

def main():
    
    ## Start video capture with the camera
    #  The argument may be changed for
    #  a path with a video
    cap=cv2.VideoCapture(0)

    ## If the camera is inaccessible, quits
    #  the execution
    #if not cap.isOpened():
    #    print("Erro ao acessar a câmera")
    #    exit(0)

    ## Sets the properties of the camera
    cap.set(3, 480)
    cap.set(4, 360)
    cap.set(5, 10)

    ## Defines the width and height of
    #  the video based on the properties of
    #  the camera
    frame_width=int(cap.get(3))
    frame_height=int(cap.get(4))
    size=(frame_width,frame_height)
    fps=cap.get(5)

    ## Configures the codec used to capture
    #  the video
    codec=cv2.VideoWriter_fourcc(*"MJPG")

    ## Creates the output object which
    #  will save the video file
    output=(
        cv2.VideoWriter(    # Video writer object
            "captura.avi",  # Output file
            codec,          # Codec
            fps,            # Frame rate
            size,           # Frame size
            True            # Color (true) or grayscale (false)
        )
    )

    ## Infinite loop
    while True:
        ## Receives the captured frame
        _,frame=cap.read()

        ## Show the captured frame
        cv2.imshow("Captura",frame)

        ## Write the frame on the output file
        output.write(frame)

        ## If the 'q' key is pressed, stops
        #  the script 
        if cv2.waitKey(1)&0XFF==ord('q'):
            break

    ## Release the capture, the output
    # and closes all windows
    cap.release()
    output.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()