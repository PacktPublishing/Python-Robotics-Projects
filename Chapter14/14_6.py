import RPi.GPIO as GPIO
import time
Import os
GPIO.setmode(GPIO.BCM)
FAN = 22
GPIO.setup(FAN,GPIO.OUT)
GPIO.output(LIGHT, GPIO.LOW)
os.system('echo "FAN TURNED OFF "|festival --tts')