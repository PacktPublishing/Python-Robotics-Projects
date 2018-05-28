import RPi.GPIO as GPIO
import time
Import os
GPIO.setmode(GPIO.BCM)
PIR = 13
GPIO.setup(PIR,GPIO.IN)
while True:

	if GPIO.input(PIR) == 1 :
 		os.system('echo "Hello, welcome to my house"|festival --tts ')
 		time.sleep(0.2)
 		os.system('echo "If you are a delivery agent then please leave the package here"|festival --tts ')
 		time.sleep(0.2)
 		os.system('echo "If you are a guest then I'm sorry I have to leave I will be back after 7pm"|festival --tts ')
 		time.sleep(0.2)
 		os.system('echo "also Kindly don't step over the grass, its freshly grown and needs some time"|festival --tts ')
 		time.sleep(1)
 		os.system('echo "Thank you !"|festival --tts ')