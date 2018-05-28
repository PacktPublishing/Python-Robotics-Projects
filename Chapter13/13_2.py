import time
import paho.mqtt.client as paho
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
broker="broker.hivemq.com"
sub_topic = light/control
client = paho.Client()
def on_message(client, userdata, message):
    print('message is : ')
    print(str(message.payload))
    data = str(message.payload)
    if data == "on":
    	GPIO.output(3,GPIO.HIGH)
    elif data == "off":
        GPIO.output(3,GPIO.LOW)

def on_connect(client,userdata, flag, rc):
    print("connection returned" + str(rc))
    client.subscribe(sub_topic)
client.connect(broker,port)
client.on_connect = on_connect
client.on_message=on_message
client.loop_forever()