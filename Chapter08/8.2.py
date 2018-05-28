import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

adc.start_adc(0, gain=GAIN)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.setwarnings(False)

servo = GPIO.PWM(14, 50)

servo.start(0)

Def Distance():
    D_value = adc0.get_last_result()
    D =    (1.0 / (F_value / 13.15)) - 0.35
    Return D

j=12.5
k=2.5
i=0

distLR=[] 
distRL=[]

while True:
        while k<=12.5:
                servo.ChangeDutyCycle(k)
                time.sleep(.1)
                distLR.insert(i,Distance())
                k = k + 2.5
                i = i + 1
        print distLR

        i=0
        k=0

        del distLR[:]

        while j>=2.5:
                servo.ChangeDutyCycle(j)
                time.sleep(.1)
                j = j - 2.5
                distRL.insert(i,Distance())
                i = i + 1

        print distRL

        i=0
        k=2.5
        j=12.5

       del distRL[:]