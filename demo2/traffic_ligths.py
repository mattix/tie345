import RPi.GPIO as GPIO
import time

LED_CAR_RED = 5
LED_CAR_YELLOW = 6
LED_CAR_GREEN = 13

LED_PEDESTRIAN_RED = 19
LED_PEDESTRIAN_GREEN = 26

BUTTON = 4

LIGHT_DELAY = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_CAR_RED, GPIO.OUT)
GPIO.setup(LED_CAR_YELLOW, GPIO.OUT)
GPIO.setup(LED_CAR_GREEN, GPIO.OUT)
GPIO.setup(LED_PEDESTRIAN_RED, GPIO.OUT)
GPIO.setup(LED_PEDESTRIAN_GREEN, GPIO.OUT)

GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def switch_to_car_red():
  GPIO.output(LED_CAR_GREEN, False)
  GPIO.output(LED_CAR_YELLOW, True)
  time.sleep(LIGHT_DELAY)
  GPIO.output(LED_CAR_YELLOW, False)
  GPIO.output(LED_CAR_RED, True)
  time.sleep(LIGHT_DELAY)
  GPIO.output(LED_PEDESTRIAN_RED, False)
  GPIO.output(LED_PEDESTRIAN_GREEN, True)

GPIO.output(LED_CAR_GREEN, True)
GPIO.output(LED_PEDESTRIAN_RED, True)

for i in range(0, 100):
  if not GPIO.input(BUTTON):
    switch_to_car_red()
  time.sleep(0.1)
