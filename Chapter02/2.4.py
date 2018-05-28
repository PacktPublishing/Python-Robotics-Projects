import time
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
LED =14

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
channel=0
adc.start_adc(channel, gain=GAIN)

while True:
    value = adc.get_last_result()
    print(str(value))
    time.sleep(0.1)
    if value >= 100:
        GPIO.output(LED,1)
    else :
        GPIO.output(LED,0)

adc.stop_adc()