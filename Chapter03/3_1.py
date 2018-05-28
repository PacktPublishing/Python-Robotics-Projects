import time
import RPi.GPIO as GPIO
import Adafruit_ADS1x15
water_valve_pin = 23
moisture_percentage = 20
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(water_valve_pin, GPIO.OUT)
adc = Adafruit_ADS1x15.ADS1115()
channel = 0
GAIN = 1
while True:
	adc.start_adc(channel, gain=GAIN)
	moisture_value = adc.get_last_result()
	moisture_value = int(moisture_value/327)
	print moisture_value
	if moisture_value < moisture_percentage:
		GPIO.output(water_valve_pin, GPIO.HIGH)
 		time.sleep(5)
	else:
		GPIO.output(water_valve_pin, GPIO.LOW)