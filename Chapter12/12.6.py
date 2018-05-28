import RPi.GPIO as GPIO
import time 
import Adafruit_DHT

GPIO.setmode(GPIO.BCM)

FAN = 18
AC = 17

pwm= GPIO.PWM(18,50)
GPIO.setup(FAN,GPIO.OUT)
GPIO.setup(AC, GPIO.OUT)

while True:

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if temperature =>20 && temperature <=30:

        Duty = 50 + ((temprature-25)*10)
        pwm.start(Duty)

    if temperature <22 :

         GPIO.output(AC, GPIO.LOW)

    if temperature >= 24

         GPIO.output(AC, GPIO.HIGH)}