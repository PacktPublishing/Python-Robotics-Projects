import signal
import flicklib
import time
import RPi.GPIO as GPIO
GIPO.setmode(GPIO.BCM)
GPIO.setup(light, GPIO.OUT)
GPIO.setup(fan,GPIO.OUT)
pwm  = GPIO.PWM(fan,100)
def message(value):
   print value
@flicklib.move()
def move(x, y, z):
   global xyztxt
   xyztxt = '{:5.3f} {:5.3f} {:5.3f}'.format(x,y,z)
@flicklib.flick()
def flick(start,finish):
   global flicktxt
   flicktxt = 'FLICK-' + start[0].upper() + finish[0].upper()
   message(flicktxt)
def main():
   global xyztxt
   global flicktxt
   xyztxt = ''
   flicktxt = ''
   flickcount = 0
   dc_inc = 0
   dc_dec = 0
   
while True:
  pwm.start(0)
  xyztxt = ' '
  if len(flicktxt) > 0 and flickcount < 5:
    flickcount += 1
  else:
    flicktxt = ''

flickcount = 0
if flicktxt ==”FLICK-WE”:
  GPIO.output(light,GPIO.LOW)
if flicktxt ==”FLICK-EW”:
  GPIO.output(light,GPIO.HIGH)
if flicktxt ==”FLICK-SN”:
  if dc_inc < 100:
    dc_inc = dc_inc + 10
    pwm.changeDutyCycle(dc_inc)

else:
  Dc_inc = 10
  if flicktxt ==”FLICK-NS”:
    if dc_inc >0:
    dc_dec = dc_dec - 10
    pwm.changeDutyCycle(dc_dec)
main()