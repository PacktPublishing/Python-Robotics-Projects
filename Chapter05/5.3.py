import time
import Adafruit_ADS1x15
import RPi.GPIO as GPIO

Motor1a =  21
Motor1b = 20
Buzzer = 14
FSR = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor1a,GPIO.OUT)
GPIO.setup(Motor1b,GPIO.OUT)
GPIO.setup(Buzzer,GPIO.OUT)
GPIO.setup(FSR,GPIO.IN)

adc = Adafruit_ADS1x15.ADS1015()

GAIN = 1
channel = 0

adc.start_adc(channel, gain=GAIN)
 
 
def Distance():
    GPIO.output(23,GPIO.LOW)

    time.sleep(0.2)

    GPIO.output(23,GPIO.HIGH)

    time.sleep(0.000010)

    GPIO.output(23,GPIO.LOW)

    while GPIO.input(24)==0:
        pulse_start = time.time()

    while GPIO.input(24)==1:
        pulse_stop = time.time()

      duration = pulse_stop - pulse_start
      distance = duration*17150.0
     distance = round(distance,2)

    return distance

while True:
   
   
   H = datetime.datetime.now().strftime('%H')

   if H == 12 or H==16 or H==20:
    value = adc.get_last_result()

    while value < 100:
        GPIO.output(BUZZER,1)
        GPIO.output(MOTOR1a,1)
        GPIO.output(MOTOR1b,0)

time.sleep(5)

GPIO.output(MOTOR1a,0)
GPIO.output(MOTOR1b,0)

if Distance() <=2 :

    GPIO.output(Buzzer, 0)
    time.sleep(5)
 
  adc.stop_adc()