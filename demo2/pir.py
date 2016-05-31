import RPi.GPIO as GPIO
import time

PIR = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

moving = False

for i in range(0, 300):
  if GPIO.input(PIR):
    if not moving:
      print("Motion started")
    moving = True
  else:
    if moving:
      print("Motion ended")
    moving = False
  time.sleep(0.1)

GPIO.cleanup()