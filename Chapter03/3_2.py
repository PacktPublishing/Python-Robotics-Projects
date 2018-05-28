from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO
import Adafruit_ADS1x15
water_valve_pin = 23
moisture_percentage = 20
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(water_valve_pin, GPIO.OUT)
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
def check_moisture():
	adc.start_adc(0,gain= GAIN)
	moisture_value = adc.get_last_result()
	moisture_value = int(moisture_value/327)
	if moisture_value < moisture_level:
		GPIO.output(water_valve_pin, GPIO.HIGH)
 		sleep(5)
 		GPIO.output(water_valve_pin, GPIO.LOW)
	else:
		GPIO.output(water_valve_pin, GPIO.LOW)
while True:
	H = datetime.now().strftime('%H')
	M = datetime.now().strftime('%M')
	if H == ‘07’ and M <= ‘10’:
 		check_moisture()
	if H == ‘17’ and M <= ‘01’:
		check_moisture()
