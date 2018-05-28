import RPi.GPIO as GPIO 
import time
GPIO.setmode(GPIO.BCM) 
GPIO.setup(23,GPIO.OUT) 
GPIO.setup(24,GPIO.IN)
while True:
	pulse_start = 0
 	pulse_stop = 0
 	duration = 0
 	distance = 0
 	GPIO.output(23,GPIO.LOW)
 	time.sleep(0.1)
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
  	print 'Distance = ',distance
  	time.sleep(0.2) 