from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO
import Adafruit_DHT
sensor = 11
pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
while True:
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	print("Temperature: " +temperature+ "C")
	print("Humidity: " +humidity+ "%")
	time.sleep(2)
