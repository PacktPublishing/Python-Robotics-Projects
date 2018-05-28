import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
LIGHT = 23
GPIO.setup(LIGHT,GPIO.OUT)
GPIO.output(LIGHT, GPIO.LOW)
os.system('echo "LIGHTS TURNED OFF "|festival --tts')