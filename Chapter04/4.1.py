import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

Motor1R = 20
Motor1L = 21

GPIO.setup(Motor1R,GPIO.OUT)
GPIO.setup(Motor1L,GPIO.OUT)


GPIO.output(Motor1R,GPIO.HIGH)
GPIO.output(Motor1L,GPIO.LOW)

sleep(5)

GPIO.output(Motor1R,GPIO.LOW)
GPIO.output(Motor1L,GPIO.HIGH)

sleep(5)

GPIO.cleanup()