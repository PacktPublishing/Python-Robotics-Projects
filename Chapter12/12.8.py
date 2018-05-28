import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

S0 = 21
S1 = 22
S2 = 23
S3 = 24

GPIO.setup(S0,GPIO.OUT)
GPIO.setup(S1,GPIO.OUT) 
GPIO.setup(S2,GPIO.OUT)

While True:

    GPIO.output(S0,1)
    GPIO.output(S1,0)
    GPIO.output(S2,1)
    GPIO.output(S4,1)

    time.sleep(1)

    GPIO.output(S0,1)
    GPIO.output(S1,1)
    GPIO.output(S2,1)
    GPIO.output(S4,1)

    time.sleep(1)

    GPIO.output(S0,1)
    GPIO.output(S1,0)
    GPIO.output(S2,0)
    GPIO.output(S4,1)

    time.sleep(1)

    'GPIO.output(S0,0)
    GPIO.output(S1,0)
    GPIO.output(S2,0)
    GPIO.output(S4,1)

    time.sleep(1)

    GPIO.output(S0,0)
    GPIO.output(S1,1)
    GPIO.output(S2,0)
    GPIO.output(S4,1)

    time.sleep(1) }