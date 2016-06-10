import picamera
import picamera.array
import time
import io

# http://picamera.readthedocs.io/en/release-1.10/recipes1.html
# http://picamera.readthedocs.io/en/release-1.10/api_array.html

imageWidth = 640
imageHeight = 360

threshold = 10
lastImageArray = None
sensitivity = 100

with picamera.PiCamera() as camera:
  camera.resolution = (imageWidth, imageHeight)
  try:
    while True:
      time.sleep(1)
      differenceCount = 0
      motionDetected = False
      with picamera.array.PiRGBArray(camera) as stream:
        camera.capture(stream, format='rgb')
        streamArray = stream.array
        if lastImageArray is not None:
          for width in range(0, imageWidth):
            if motionDetected:
              break
            for height in range(0, imageHeight):
              if motionDetected:
                break
              difference = abs(int(streamArray[height][width][1]) - int(lastImageArray[height][width][1]))
              if  difference > threshold:
                differenceCount += 1
            if differenceCount > sensitivity:
              motionDetected = True
        lastImageArray = streamArray
        if motionDetected:
          print("Motion detected")
  finally:
    camera.close()