import RPi.GPIO as GPIO
import time                             
GPIO.setmode(GPIO.BCM)       
GPIO.setup(18,GPIO.OUT)         
I = 0
pwm= GPIO.PWM(18,50)

for I < 100:

    I = I+1
    pwm.start(I)
    time.sleep(0.1)


GPIO.cleanup()}