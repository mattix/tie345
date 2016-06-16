import numpy as np
import cv2

# http://docs.opencv.org/3.1.0/d7/d8b/tutorial_py_face_detection.html

image = cv2.imread('Linus_Torvalds_talking.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imwrite("detected_faces.jpg", image);