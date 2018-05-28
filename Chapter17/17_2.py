import smbus
from time import sleep
import RPi.GPIO as GPIO
int1 = 12
int2 = 16
int3 = 18
int4 = 15
GPIO.setup(int1, GPIO.OUT)
GPIO.setup(int2, GPIO.OUT)
GPIO.setup(int3, GPIO.OUT)
GPIO.setup(int4, GPIO.OUT)
PWM1 = GPIO.PWM(12, 100)
PWM2 = GPIO.PWM(16, 100)
PWM3 = GPIO.PWM(18, 100)
PWM4 = GPIO.PWM(15, 100)
PWM1.start(0)
PWM2.start(0)
PWM3.start(0)
PWM4.start(0)
PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
INT_ENABLE = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47

def MPU_Init():
	bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
	bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
	bus.write_byte_data(Device_Address, CONFIG, 0)
	bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
	bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
	high = bus.read_byte_data(Device_Address, addr)
 	low = bus.read_byte_data(Device_Address, addr+1)
 	value = ((high << 8) | low)
 	if(value > 32768):
 		value = value - 65536
 		return value
	bus = smbus.SMBus(1)
	Device_Address = 0x68

MPU_Init()
while True:
 	acc_x = read_raw_data(ACCEL_XOUT_H)
 	acc_y = read_raw_data(ACCEL_YOUT_H)
 	acc_z = read_raw_data(ACCEL_ZOUT_H)
 	gyro_x = read_raw_data(GYRO_XOUT_H)
 	gyro_y = read_raw_data(GYRO_YOUT_H)
 	gyro_z = read_raw_data(GYRO_ZOUT_H)
 	Ax = (gyro_x/327)
 	Ay = (gyro_y/327)
 	for Ax > 20:
 		PWM1.changeDutyCycle(Ax)
 		PWM3.changeDutyCycle(Ax)
 	for Ax < -20:
 		PWM2.changeDutyCycle(Ax)
 		PWM4.changeDutyCycle(Ax)

 	for Ay > 20:
 		PWM1.changeDutyCycle(Ax)
 		PWM4.changeDutyCycle(Ax)
 	for Ay < -20:
 		PWM2.changeDutyCycle(Ax)
 		PWM3.changeDutyCycle(Ax)
