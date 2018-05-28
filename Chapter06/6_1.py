import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
Motor1a = 20
Motor1b = 21
Motor2a = 2
Motor2b = 3
GPIO.setup(Motor1a,GPIO.OUT)
GPIO.setup(Motor1b,GPIO.OUT)
GPIO.setup(Motor2a,GPIO.OUT)
GPIO.setup(Motor2b,GPIO.OUT)
GPIO.output(Motor1a,1)
GPIO.output(Motor1b,0)
GPIO.output(Motor2a,1)
GPIO.output(Motor2b,0)
time.sleep(10)
GPIO.cleanup()