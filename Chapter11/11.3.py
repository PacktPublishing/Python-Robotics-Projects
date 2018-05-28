import RPi.GPIO as GPIO
import time 

import Adafruit_ADS1x15
adc0 = Adafruit_ADS1x15.ADS1115()

GAIN = 1

adc0.start_adc(0, gain=GAIN)

LIGHT = 23
PIR = 24
Irritation_flag = 1
IR = 2

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(LIGHT,GPIO.OUT) 
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(IR. GPIO.IN)

import datetime

H = datetime.datetime.now().strftime('%H') 
M = datetime.datetime.now().strftime('%M')


  while True:

  if H = '07' and M <= '15' and Iriitation_Flag > 0 and GPIO.input(PIR) == 0:

      GPIO.output(LIGHT,GPIO.HIGH)


  if H = '07'and GPIO.input(PIR)==1:
    
   M_snooze = datetime.datetime.now().strftime('%M')
   M_snooze = M_snooze + 5
  
   for M <= M_snooze 
    
     GPIO.output(LIGHT,GPIO.LOW)

     F_value = adc0.get_last_result()
     F1 =    (1.0 / (F_value / 13.15)) - 0.35

     time.sleep(0.1)
   
     F_value = adc0.get_last_result()
     F2 =    (1.0 / (F_value / 13.15)) - 0.35

     F_final = F1-F2

     M = datetime.datetime.now().strftime('%M')

     if F_final > 25
 
         Irritation_flag = 0



  for H = '07'and M > '15' and Irritation_Flag > 0 and GPIO.input(PIR) = 0:

 GPIO.output(LIGHT,GPIO.HIGH)
 time.sleep(5)
 GPIO.output(LIGHT,GPIO.LOW)
 time.sleep(5)
 
 if H != '07':
 
 Irritation_flag = 1