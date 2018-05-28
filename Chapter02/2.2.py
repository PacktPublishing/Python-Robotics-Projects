import time import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN) 
GPIO.setup(24,GPIO.OUT)
while True:
 if GPIO.input(23) == 1: 
	GPIO.output(24,GPIO.HIGH)
 else: 
	GPIO.output(24,GPIO.LOW)

 time.sleep(1)
GPIO.cleanup()