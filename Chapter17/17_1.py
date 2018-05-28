import smbus
from time import sleep
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
print (" Reading Data of Gyroscope and Accelerometer")
while True:
 	Ax = read_raw_data(ACCEL_XOUT_H)
 	Ay = read_raw_data(ACCEL_YOUT_H)
 	Az = read_raw_data(ACCEL_ZOUT_H)
 	Gx = read_raw_data(GYRO_XOUT_H)
 	Gy = read_raw_data(GYRO_YOUT_H)
 	Gz = read_raw_data(GYRO_ZOUT_H)
	print(“Ax=”+str(Ax)+”Ay=”+str(Ay)+"Az="+str(Az)+“Gx=”+str(Gx)+”Gy=”+str(Gy)+"Gz="+str(Gz))