import Adafruit_DHT
import time
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
from datetime import datetime

KEY_FILE = 'tiea345-aee5c60ede2b.json'
SPREADSHEET_NAME = 'ahinko_tiea345_demo3'

SENSOR = Adafruit_DHT.DHT11
PIN = 4

json_key = json.load(open(KEY_FILE))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

def add_line(line):
  gc = gspread.authorize(credentials)
  wks = gc.open(SPREADSHEET_NAME).sheet1
  wks.append_row(line)

humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)

while True:
  if humidity is not None and temperature is not None:
    add_line([datetime.now().isoformat(), temperature, humidity])
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
  time.sleep(60)