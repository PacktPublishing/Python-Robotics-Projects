import RPi.GPIO as GPIO
import time
 
LIGHT = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LIGHT,GPIO.OUT)
 
import datetime

H = datetime.datetime.now().strftime('%H')
M = datetime.datetime.now().strftime('%M') 

   
while True:

       if H = '06'and M < 20 :
           GPIO.output(LIGHT,GPIO.HIGH)

       else:
           GPIO.output(LIGHT,GPIO.LOW)