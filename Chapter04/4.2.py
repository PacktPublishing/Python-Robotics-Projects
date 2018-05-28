import RPi.GPIO as GPIO
from time
import sleep
GPIO.setmode(GPIO.BCM)

Motor1R = 20
Motor1L = 21

GPIO.setup(Motor1R, GPIO.OUT)
GPIO.setup(Motor1L, GPIO.OUT)

pwm = GPIO.PWM(Motor1R, 100)
pwm.start(0)

try:
while True:
  GPIO.output(Motor1L, GPIO.LOW)
for i in range(0, 101):
  pwm.ChangeDutyCycle(i)
sleep(0.1)

except KeyboardInterrupt:

  pwm.stop()
GPIO.cleanup()