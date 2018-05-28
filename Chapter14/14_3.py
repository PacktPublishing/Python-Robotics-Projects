import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
LIGHT = 2
GPIO.setup(LIGHT,GPIO.OUT)
GPIO.output(LIGHT, GPIO.HIGH)
os.system('echo "LIGHTS TURNED ON "|festival --tts')