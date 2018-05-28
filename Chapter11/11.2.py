import RPi.GPIO as GPIO
import time 

LIGHT = 23
PIR = 24
Irritation_flag = 3

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(LIGHT,GPIO.OUT) 
GPIO.setup(PIR, GPIO.IN)

import datetime

H = datetime.datetime.now().strftime('%H') 
M = datetime.datetime.now().strftime('%M')


    while True:

        if H = '07' and M <= '15' and Iriitation_Flag > 0 and GPIO.input(PIR) == 0:

            GPIO.output(LIGHT,GPIO.HIGH)


        if H = '07'and GPIO.input(PIR)==1:

            GPIO.output(LIGHT,GPIO.LOW)
            time.sleep(10)
            Irritation_Flag = Irritation_Flag - 1


        for H = '07'and M > '15' and Irritation_Flag > 0 and GPIO.input(PIR) = 0:

            GPIO.output(LIGHT,GPIO.HIGH)
            time.sleep(5)
            GPIO.output(LIGHT,GPIO.LOW)
            time.sleep(5)
            

        if H != '07':
            
            Irritation_flag = 3
            GPIOP.output(LIGHT, GPIO.LOW)