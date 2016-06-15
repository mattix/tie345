import numpy as np
import cv2
from matplotlib import pyplot as plt

# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/\
# py_feature2d/py_orb/py_orb.html
# http://docs.opencv.org/master/dc/dc3/tutorial_py_matcher.html

image1 = cv2.imread('23243020106_0c94e200c5_z.jpg',0)
image2 = cv2.imread('23754539739_16ae62c6f7_z.jpg',0)

orb = cv2.ORB_create()

keypoints1 = orb.detect(image1, None)
keypoints2 = orb.detect(image2, None)

keypoints1, description1 = orb.compute(image1, keypoints1)
keypoints2, description2 = orb.compute(image2, keypoints2)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(description1,description2)
matches = sorted(matches, key = lambda x:x.distance)
image3 = cv2.drawMatches(
    image1,keypoints1,image2,keypoints2,matches, None, flags=2)

#plt.imshow(image3),plt.show()
cv2.imwrite("output.jpg", image3);