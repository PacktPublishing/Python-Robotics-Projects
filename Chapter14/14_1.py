import os
from time import sleep
os.system('echo "hello! i am raspberry pi robot"|festival --tts ')
sleep(2)
os.system('echo "how are you?"| festival --tts ')
sleep(2)
os.system('echo "I am having fun."| festival --tts ')
sleep(2)