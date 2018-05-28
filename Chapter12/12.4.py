import GPIO library
   import RPi.GPIO as GPIO
   import time
   import time
   import Adafruit_ADS1x15
   adc0 = Adafruit_ADS1x15.ADS1115()
GAIN = 1
 adc0.start_adc(0, gain=GAIN)
adc1.start_adc(1, gain=GAIN)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PCount = 0
while True:
   F_value = adc0.get_last_result()
   F1 =    (1.0 / (F_value / 13.15)) - 0.35
   time.sleep(0.1)
   F_value = adc0.get_last_result()
   F2 =    (1.0 / (F_value / 13.15)) - 0.35
   F0_final = F1-F2
   if F0 > 10 :
        Time0 =  time.time()
   F_value = adc1.get_last_result()
   F1 =    (1.0 / (F_value / 13.15)) - 0.35
   time.sleep(0.1)
   F_value = adc1.get_last_result()
   F2 =    (1.0 / (F_value / 13.15)) - 0.35
   F1_final = F1-F2
   if F1 > 10:
        Time1 =  time.time()
    if Time1 > Time0:
        PCount = PCount + 1
    if Time1 < Time0:
        PCount = PCount - 1

if PCount > 0:

           GPIO.output(LIGHT, GPIO.HIGH)
       else if PCount = 0:
          GPIO.output(LIGHT, GPIO.LOW)
