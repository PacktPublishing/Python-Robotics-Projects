import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

 
GPIO.setwarnings(False)

pwm1 = GPIO.PWM(14, 50)
pwm2 = GPIO.PWM(16, 50)
pwm3 = GPIO.PWM(18, 50)
pwm4 = GPIO.PWM(20, 50)
pwm5 = GPIO.PWM(21, 50)
pwm6 = GPIO.PWM(22, 50)
 
pwm1.start(cvt_angle(90))
pwm2.start(cvt_angle(90))
pwm3.start(cvt_angle(90))
pwm4.start(cvt_angle(90))
pwm5.start(cvt_angle(90))
pwm6.start(cvt_angle(90))

def cvt_angle(angle):
    dc = float(angle/90) + 0.5
    return dc

while True:

    a = raw_input("enter a list of 6 values")
    
    if a[0] < 160 and  a[0] > 30:
        pwm1.ChangeDutyCycle(cvt_angle(a[0]))

    if a[1] < 160 and  a[1] > 30:
        pwm2.ChangeDutyCycle(cvt)angle(a[1]))

    if a[0] < 160 and  a[0] > 30:
        pwm3.ChangeDutyCycle(cvt_angle(a[2]))

    if a[0] < 160 and  a[0] > 30:
        pwm4.ChangeDutyCycle(cvt_angle(a[3]))

    if a[0] < 160 and  a[0] > 30:
        pwm5.ChangeDutyCycle(cvt_angle(a[4]))

    if a[0] < 160 and  a[0] > 30:
        pwm6.ChangeDutyCycle(cvt_angle(a[5]))}