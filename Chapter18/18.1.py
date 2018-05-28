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
 
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)
pwm5.start(0)
pwm6.start(0)

def cvt_angle(angle):
    dc = float(angle/90) + 0.5
    return dc

while 1:

 j = input('select servo')

 if j == 1:

  i = input('select value to rotate')
  pwm1.ChangeDutyCycle(cvt_angle(i))
  time.sleep(2)
  pwm1.ChangeDutyCycle(cvt_angle(90))

 elif j ==2:
 
  i = input('select value to rotate')
  pwm2.ChangeDutyCycle(cvt_angle(i))
  time.sleep(2)
  pwm2.ChangeDutyCycle(cvt_angle(90))


 elif j ==3:

 i = input('select value to rotate')
 pwm3.ChangeDutyCycle(cvt_angle(i))
 time.sleep(2)
 pwm3.ChangeDutyCycle(cvt_angle(90))

 elif j ==4: 

 i = input('select value to rotate')
 pwm4.ChangeDutyCycle(cvt_angle(i))
 time.sleep(2)
 pwm4.ChangeDutyCycle(cvt_angle(90))

 elif j ==5:
 
 i = input('select value to rotate')
 pwm5.ChangeDutyCycle(cvt_angle(i))
 time.sleep(2)
 pwm5.ChangeDutyCycle(cvt_angle(90))

 elif j ==6:
 
 i = input('select value to rotate')
 pwm6.ChangeDutyCycle(cvt_angle(i))
 time.sleep(2)
 pwm6.ChangeDutyCycle(cvt_angle(90)) }