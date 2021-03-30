# opencv-basic
Collection of basic OpenCV applications.

## display_video.py
The simplest opencv application, it captures video from th camera and displays it.

## mog2.py
Uses a background subtraction technique to detect moving objects.

## haar_cascade.py
Uses the haar cascade algorythm to detect faces.

## save_video.py
Captures the video from a camera and saves it to a file.

## treading_display.py
Display the video from the camera using threading.

## treading_record.py (TODO)
Records the capture from the camera using threading.

## encode_faces.py/facial_recognition.py
Face encoding/recognition scripts. First one Processes and encodes the faces in a database and saves the result in a file. The second one make the facial recognition through the camera. Both must have arguments passed on:

encode_faces.py
* --dataset: folder with the collection of pictures (pictures must be in a folder with the person's name within the main dataset folder);
* --encodings: file to which the face encoding will be dumped;
* --detection-method: which method will be used (hog/cnn).
~~~
python3 encode_faces.py --dataset dataset --encodings encodings.pickle --detection-method hog
~~~

facial_recognition.py
* --cascade: file with the haar cascade for face detection;
* --encodings: file that contains the face encodings
~~~
python3 pi_face_recognition.py --cascade haar_cascade/haarcascade_frontalface_default.xml --encodings encodings.pickle
~~~

### Dependencies:
The projects were scripted with Python 3.8.5 and the following packages:

~~~
astroid==2.4.2
isort==5.6.4
lazy-object-proxy==1.4.3
mccabe==0.6.1
numpy==1.19.4
imutils==0.5.4
opencv-python==4.4.0.46
opencv-contrib-python
pkg-resources==0.0.0
pylint==2.6.0
six==1.15.0
toml==0.10.2
typed-ast==1.4.1
wrapt==1.12.1
dlib==19.22.0
face-recognition==1.3.0
face-recognition-models==0.3.0
Pillow==8.1.2
~~~