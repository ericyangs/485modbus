# -*- coding:utf-8 -*-
#import RPi.GPIO as GPIO
import serial
import minimalmodbus

#EN_485 =  4
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(EN_485,GPIO.OUT)
#GPIO.output(EN_485,GPIO.HIGH)
#電流模式
def calcFromA(max,min,data):
    return ((max-min)/16)*(data-4)+min
#電壓模式
def calcFromV(max,min,data):
    return ((max-min)/10)*data+min



try:
	#conn=minimalmodbus.Instrument('/dev/ttyS0',1)
	conn=minimalmodbus.Instrument('COM6',1)

	conn.serial.baudrate=9600
	conn.serial.bytesize=8
	conn.serial.parity=serial.PARITY_NONE
	conn.serial.stopbits=1
	conn.serial.timeout=0.1
	conn.mode=minimalmodbus.MODE_ASCII


	#read_bit function 1, 2 , read one bit only
	#format
	#read_bit(address start, function code)
	conn.address=97
	#conn.read_register( 1, 2, 4 ,signed=True)



	#(((sensor感測範圍上限-sensor感測範圍下限)/16) *讀值 )+sensor感測範圍下限

	tep=conn.read_register(2,3,4,signed=False)
	print(tep)
	tec=calcFromA(100,0,tep)
	print(tec)
	#print (calcFromA(50,0,14.2))

	#do relay on off
	#write_bit function code 5, 15
	#format
	#write_bit(address,value,function code)
	#conn.address=33
	#conn.write_bit(1,0,15)



except Exception as e:
   print("error:" + str(e))
#finally:
	#GPIO.cleanup()
