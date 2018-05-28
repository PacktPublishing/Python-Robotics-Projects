import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIR = 24
LIGHT = 23
GPIO.setup(DOPPLER,GPIO.IN)
GPIO.setup(BUZZER,GPIO.OUT)
While True:
     if GPIO.input(PIR) == 1:
         GPIO.output(LIGHT,GPIO.HIGH)    
     if GPIO.input(PIR) == 0:
         GPIO.output(LIGHT,GPIO.LOW)