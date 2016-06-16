import numpy as np
import cv2
import picamera
import picamera.array
import time
 
with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        time.sleep(0.1)

        camera.capture(stream, format="bgr")
        image = stream.array
         
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imwrite("detected_faces_from_cam.jpg", image);