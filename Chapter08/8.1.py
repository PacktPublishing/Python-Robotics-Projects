import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)

pwm = GPIO.PWM(14, 50)
pwm.start(0)

while 1:

        pwm.ChangeDutyCycle(2.5)
        time.sleep(2)

        pwm.ChangeDutyCycle(5)
        time.sleep(2)

        pwm.ChangeDutyCycle(7.5)
        time.sleep(2)

        pwm.ChangeDutyCycle(10)
        time.sleep(2)

        pwm.ChangeDutyCycle(12.5)
        time.sleep(2)