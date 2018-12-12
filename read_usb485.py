# -*- coding:utf-8 -*-
import serial
import minimalmodbus

def calcFromA(max,min,data):
    return ((max-min)/16)*(data-4)+min

def calcFromV(max,min,data):
    return ((max-min)/10)*data+min

try:
	conn=minimalmodbus.Instrument('COM6',1)
	conn.serial.baudrate=9600
	conn.serial.bytesize=8
	conn.serial.parity=serial.PARITY_NONE
	conn.serial.stopbits=1
	conn.serial.timeout=0.1
	conn.mode=minimalmodbus.MODE_ASCII

	conn.address=97
	tep=conn.read_register(2,3,4,signed=False)
	print(tep)
	tec=calcFromA(100,0,tep)
	print(tec)

except Exception as e:
   print("error:" + str(e))
