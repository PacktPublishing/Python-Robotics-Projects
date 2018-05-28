import Adafruit_ADS1x15
import RPi.GPIO as GPIO

adc = Adafruit_ADS1x15.ADS1015()

GAIN = 1
channel = 0

adc.start_adc(channel, gain=GAIN)

while True:
   
    print(adc.get_last_result())