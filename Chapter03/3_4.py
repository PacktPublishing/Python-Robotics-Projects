from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO
import Adafruit_ADS1x15
import Adafruit_DHT
water_valve_pin = 23
sensor = 11
pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(water_valve_pin, GPIO.OUT)
Channel =0
GAIN = 1
adc = Adafruit_ADS1x15.ADS1115()
def check_moisture(m):
	adc.start_adc(channel, gain=GAIN)
	moisture_value = adc.get_last_result()
	moisture_value = int(moisture_value/327)
	print moisture_value

	if moisture_value < m:
		GPIO.output(water_valve_pin, GPIO.HIGH)
		sleep(5)
		GPIO.output(water_valve_pin, GPIO.LOW)
	else:
		GPIO.output(water_valve_pin, GPIO.LOW)
		
while True:
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	H = datetime.now().strftime(‘%H’)
	M = datetime.now().strftime(‘%M’)
	if H == ‘07’ and M <= ‘10’:
		if temperature < 15:
 			check_moisture(20)
		elif temperature >= 15 and temperature < 28:
 			check_moisture(30)
		elif temperature >= 28:
			check_moisture(40)
	if H == ‘17’ and M <= ‘10’:
		if temperature < 15:
			check_moisture(20)
		elif temperature >= 15 and temperature < 28:
 			check_moisture(30)
		elif temperature >= 28:
			check_moisture(40)
