import Adafruit_ADS1x15
import RPi.GPIO as GPIO
import time
Motor1a = 21
Motor1b = 20
Buzzer = 14
FSR = 16
THRESHOLD = 1000
GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor1a,GPIO.OUT)
GPIO.setup(Motor1b,GPIO.OUT)
GPIO.setup(Buzzer,GPIO.OUT)
GPIO.setup(FSR,GPIO.IN)
adc = Adafruit_ADS1x15.ADS1015()
GAIN = 1
channel = 0
adc.start_adc(channel, gain=GAIN)
while True:
 M = datetime.datetime.now().strftime('%M')
 if (H == 12 or H==16 or H==20) && M == 00 :
 value = adc.get_last_result()
 while value < THRESHOLD:
 GPIO.output(BUZZER,1)
 GPIO.output(MOTOR1a,1)
 GPIO.output(MOTOR1b,0)
 GPIO.output(MOTOR1a,0)
 GPIO.output(MOTOR1b,1)
 GPIO.output(Buzzer,0)
 time.sleep(5)
 GPIO.output(MOTOR1b,0)
adc.stop_adc()