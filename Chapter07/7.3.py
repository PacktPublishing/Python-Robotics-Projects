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

def right():
        GPIO.output(Motor1a,0)
        GPIO.output(Motor1b,1)
        GPIO.output(Motor2a,1)
        GPIO.output(Motor2b,0)

def left():
        GPIO.output(Motor1a,1)
        GPIO.output(Motor1b,0)
        GPIO.output(Motor2a,0)
        GPIO.output(Motor2b,1)

def stop():
        GPIO.output(Motor1a,0)
        GPIO.output(Motor1b,0)
        GPIO.output(Motor2a,0)
        GPIO.output(Motor2b,0)

while True:

   forward()

   F_value = adc0.get_last_result()
   F =   (1.0 / (F_value / 13.15)) - 0.35

   min_dist = 20
   if F< min_dist:

        stop()

    right()
    time.sleep(1)

    F_value = adc0.get_last_result()
    F =    (1.0 / (F_value / 13.15)) - 0.35
    R = F

    left()
    time.sleep(2)

    F_value = adc0.get_last_result()
    F =    (1.0 / (F_value / 13.15)) - 0.3

    L = F

    if L < R:
        right()
        time.sleep(2)

    else:
        forward()