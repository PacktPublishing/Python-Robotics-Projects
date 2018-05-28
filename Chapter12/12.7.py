import RPi.GPIO as GPIO
import time 
import Adafruit_DHT

GPIO.setmode(GPIO.BCM)

FAN = 18
AC = 17
PIR = 22
PIN = 11
Sensor = 4

pwm= GPIO.PWM(18,50)
GPIO.setup(FAN,GPIO.OUT)
GPIO.setup(AC, GPIO.OUT)

while True:

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    H = datetime.datetime.now().strftime('%H') 
    M = datetime.datetime.now().strftime('%M')

    if H <= 6 && H <= 22:

        if M <=58 :

           M = datetime.datetime.now().strftime('%M')
           humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
           
           if GPIO.input(PIR) == 0 :
                
                Movement = Movement + 1
                time.sleep(10)

           if temperature < 28:
        
                if Movement > 5 :

                    Duty = Duty + 10
                    pwm.start(Duty)
                    Movement = 0     

        if M = 59 : 

            if Movement = 0 :

                Duty = Duty -10
                pwm.start(Duty)

            Movement = 0

        if temperature <22 :

           GPIO.output(AC, GPIO.LOW)

       if temperature >= 24 && H <= 6 && H >= 22:

           GPIO.output(AC, GPIO.HIGH)

        if temperature > 27

            pwm.start(100)

    for H > 7 && H < 20 

        GPIO.output(AC, GPIO.LOW)

    if H = 20 

        GPIO.output(AC,GPIO.HIGH)
}