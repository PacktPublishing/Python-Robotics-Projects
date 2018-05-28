import RPi.GPIO as GPIO
import time
Import os
GPIO.setmode(GPIO.BCM)
FAN = 22
GPIO.setup(FAN,GPIO.OUT)
GPIO.output(LIGHT, GPIO.HIGH)
os.system('echo "FAN TURNED ON "|festival --tts')
