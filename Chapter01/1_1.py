import time 
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT) 
GPIO.setup(24, GPIO.IN) 
GPIO.setup(22, GPIO.OUT)
while True:
    button_state = GPIO.input(24)
    if(button_state == True):
        GPIO.output(23,GPIO.HIGH)
    else:
        GPIO.output(23,GPIO.LOW)
    time.sleep(0.5)