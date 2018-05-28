import time
import paho.mqtt.client as mqtt
import RPi.gpio as gpio
pir = 23
gpio.setmode(gpio.BCM)
gpio.setup(pir, gpio.IN)
client = mqtt.Client()
broker="broker.hivemq.com"
port = 1883
pub_topic = "IntruderDetector_Home"
def SendData():
  client.publish(pub_topic,"WARNING : SOMEONE DETECTED AT YOUR PLACE")

def on_connect(client, userdata, flag,rc):
  print("connection returned" + str(rc))
  SendData()
while True:
  client.connect(broker,port)
  client.on_connect = on_connect
  if gpio.output(pir) == gpio.HIGH :
    SendData()
  client.loop_forever()
