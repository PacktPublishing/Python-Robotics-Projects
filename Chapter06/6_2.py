import bluetooth
import time
import RPi.GPIO as GPIO
Motor1a = 20
Motor1b = 21
Motor2a = 2
Motor2b = 3
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(Motor1a,GPIO.OUT)
GPIO.setup(Motor1b,GPIO.OUT)
GPIO.setup(Motor2a,GPIO.OUT)
GPIO.setup(Motor2b,GPIO.OUT)
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
port = 1
server_socket.bind(("",port))
server_socket.listen(1)
client_socket,address = server_socket.accept()
print ("Accepted connection from "+str(address))
def stop_car():
  GPIO.output(Motor1a,0)
  GPIO.output(Motor1b,0)
  GPIO.output(Motor2a,0)
  GPIO.output(Motor2b,0)

while True:
  data = client_socket.recv(1024)
  if (data == "B" or data== "b"):
    GPIO.output(Motor1a,1)
    GPIO.output(Motor1b,0)
    GPIO.output(Motor2a,1)
    GPIO.output(Motor2b,0)
    time.sleep(1)
    stop_car()

  if (data == "F" or data == "f"):
    GPIO.output(Motor1a,0)
    GPIO.output(Motor1b,1)
    GPIO.output(Motor2a,0)
    GPIO.output(Motor2b,1)
    time.sleep(1)
    stop_car()

  if (data == "R" or data == "r"):
    GPIO.output(Motor1a,0)
    GPIO.output(Motor1b,1)
    GPIO.output(Motor2a,1)
    GPIO.output(Motor2b,0)
    time.sleep(1)
    stop_car()

  if (data == "L" or data == "l"):
    GPIO.output(Motor1a,1)
    GPIO.output(Motor1b,0)
    GPIO.output(Motor2a,0)
    GPIO.output(Motor2b,1)
    time.sleep(1)
    stop_car()

  if (data == "Q" or data =="q"):
    stop_car()
    
  if (data =='Z' or data == "z"):
    client_socket.close()
    server_socket.close()
