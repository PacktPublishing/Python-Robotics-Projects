import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIR = 24
LIGHT = 23
TIME = 5

GPIO.setup(PIR,GPIO.IN)
GPIO.setup(BUZZER,GPIO.OUT)

While True:

   If GPIO.input(PIR) == 1:
       
       M = datetime.datetime.now().strftime('%M')
       M_final= M + TIME

       for M < M_final:

         GPIO.output(LIGHT,GPIO.HIGH)
         M = datetime.datetime.now().strftime('%M')

         if GPIO.input(PIR) == 1:
            M_final = M_final + 1 


    if GPIO.input(PIR) = 0:

        GPIO.output(LIGHT, GPIO.LOW)}