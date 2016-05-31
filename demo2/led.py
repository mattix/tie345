import RPi.GPIO as GPIO
import time

LED = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

for i in range(0, 20):
  GPIO.output(LED, i % 2)
  time.sleep(1)

GPIO.cleanup()