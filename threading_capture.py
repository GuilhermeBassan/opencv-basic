from threading import Thread, Lock
import cv2



## Initializes the threaded camera stream
class WebcamVideoCapture:
    
    def __init__(self,src=0,width=320,height=240,fps=15):
        self.stream=cv2.VideoCapture(src)
        self.stream.set(cv2.CAP_PROP_FRAME_WIDTH,width)
        self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
        self.stream.set(cv2.CAP_PROP_FPS,fps)

        self.width=self.stream.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height=self.stream.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.fps=self.stream.get(cv2.CAP_PROP_FPS)

        (self.grabbed,self.frame)=self.stream.read()
        self.started=False
        self.read_lock=Lock()

    def start(self) :
        if self.started :
            print("already started!!")
            return None
        self.started = True
        self.thread = Thread(target=self.update, args=())
        self.thread.start()
        return self

    def get_parameters(self):
        return (
            self.width,
            self.height,
            self.fps
        )

    def update(self) :
        while self.started :
            (grabbed, frame) = self.stream.read()
            self.read_lock.acquire()
            self.grabbed, self.frame = grabbed, frame
            self.read_lock.release()

    def read(self) :
        self.read_lock.acquire()
        frame = self.frame.copy()
        self.read_lock.release()
        return frame

    def stop(self) :
        self.started = False
        self.thread.join()

    def __exit__(self, exc_type, exc_value, traceback) :
        self.stream.release()

def main():
    vs = WebcamVideoCapture().start()

    width,height,fps=vs.get_parameters()
    size=(width,height)
    
    codec=cv2.VideoWriter_fourcc(*"MJPG")
    output=(
        cv2.VideoWriter(    # Video writer object
            "captura.avi",  # Output file
            codec,          # Codec
            fps,            # Frame rate
            size,           # Frame size
            True            # Color (true) or grayscale (false)
        )
    )

    while True :
        frame = vs.read()
        cv2.imshow('Webcam', frame)
        output.write(frame)

        if cv2.waitKey(1) == 27 :
            break

    vs.stop()
    output.release()
    cv2.destroyAllWindows()

if __name__ == "__main__" :
    main()