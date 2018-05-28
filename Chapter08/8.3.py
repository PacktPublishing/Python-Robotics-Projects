import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15

adc0 = Adafruit_ADS1x15.ADS1115()
GAIN = 1
adc0.start_adc(0, gain=GAIN)

GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)

servo = GPIO.PWM(14, 50)
servo.start(0)

def Distance():
    D_value = adc0.get_last_result()
    D =    (1.0 / (F_value / 13.15)) - 0.35
    Return D

GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

LForward = GPIO.PWM(20, 50)
LReverse = GPIO.PWM(21, 50)
RForward = GPIO.PWM(23,50)
RReverse = GPIO.PWM(24,50)

def stop():
    LForward.changeDutyCycle(0)
    LReverse.changeDutyCycle(0)
    RForward.changeDutyCycle(0)
    RReverse.changeDutyCycle(0)


def direction(index):

 if index == 0 :
    LForward.changeDutyCycle(0)
    LReverse.changeDutyCycle(30)
    RForward.changeDutyCycle(30)
    RReverse.changeDutyCycle(0)

elif index == 1

    LForward.changeDutyCycle(20)
    LReverse.changeDutyCycle(0)
    RForward.changeDutyCycle(50)
    RReverse.changeDutyCycle(0)

 elif index == 2 :

    LForward.changeDutyCycle(50)
    LReverse.changeDutyCycle(0)
    RForward.changeDutyCycle(50)
    RReverse.changeDutyCycle(0)

elif index == 3 :

    LForward.changeDutyCycle(50)
    LReverse.changeDutyCycle(0)
    RForward.changeDutyCycle(20)
    RReverse.changeDutyCycle(0)


 elif index == 4 :

    LForward.changeDutyCycle(20)
    LReverse.changeDutyCycle(0)
    RForward.changeDutyCycle(0)
    RReverse.changeDutyCycle(20)

 else:
 stop()

j=12.5
k=2.5
i=0

dist1=[]
dist2=[]

while True:

    while k<=12.5:
    servo.ChangeDutyCycle(k)
    time.sleep(.2)
    dist1.insert(i,Distance())
    k = k + 2.5
    i = i + 1

 print dist1

 i=0
 k=2

 max_dist1 = max(dist1)
 max_dist1_index = dist1.index(max_dist1)

 direction(max_dist1_index)

 del dist1[:]

 print max_dist1
 print max_dist1_index

 while j>=2.5:
    servo.ChangeDutyCycle(j)
    time.sleep(.2)
     j = j - 2.5
     dist2.insert(i,Distance())
    i = i + 1
 
print dist2

i=0
j=12

 max_dist2 = max(dist2)
 max_dist2_index = dist2.index(max_dist2)

 direction(max_dist2_index)

 del dist2[:]

 print max_dist2
 print max_dist2_index