import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

import Adafruit_ADS1x15
adc0 = Adafruit_ADS1x15.ADS1115()

GAIN = 1

adc0.start_adc(0, gain=GAIN)

Motor1a = 20
Motor1b = 21
Motor2a = 23
Motor2b = 24

GPIO.setup(Motor1a,GPIO.OUT)
GPIO.setup(Motor1b,GPIO.OUT)
GPIO.setup(Motor2a,GPIO.OUT)
GPIO.setup(Motor2b,GPIO.OUT)

def forward():
        GPIO.output(Motor1a,0)
        GPIO.output(Motor1b,1)
        GPIO.output(Motor2a,0)
        GPIO.output(Motor2b,1)

def turn():
        GPIO.output(Motor1a,0)
        GPIO.output(Motor1b,1)
        GPIO.output(Motor2a,1)
        GPIO.output(Motor2b,0)
)

while True:
   forward()

   F_value = adc0.get_last_result()
   F =    (1.0 / (F_value / 13.15)) - 0.35
 
    min_dist = 20

    while F < min_dist:
        turn()   