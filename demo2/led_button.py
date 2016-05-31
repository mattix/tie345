import RPi.GPIO as GPIO
import time

# http://razzpisampler.oreilly.com/ch07.html
# When button is presset, GPIO.input returns False

LED = 4
BUTTON = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for i in range(0, 100):
  GPIO.output(LED, not GPIO.input(BUTTON)) # Negate input
  time.sleep(0.1)

GPIO.cleanup()