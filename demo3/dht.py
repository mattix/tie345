import Adafruit_DHT
import time

SENSOR = Adafruit_DHT.DHT11
PIN = 4

humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)

while True:
  if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
  time.sleep(1)