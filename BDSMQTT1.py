#encoding:UTF-8
import struct, os
import serial
import time
import re
import sys
#from test1 import send_server

ser = serial.Serial("/dev/ttyS0",9600,timeout = 1)
def reboot():
        
        print("Waiting for module\n")
        time.sleep(0.5)
        comdata = ""
        ser.write(("AT\r\n").encode('utf-8'))
        while (comdata.find("OK")== -1):
                time.sleep(0.1)
                while (ser.inWaiting()>0):
                        comdata = ser.read(ser.inWaiting())
                        comdata = comdata.decode("ascii")
                        comdata = comdata.strip()
                        print(comdata)
                        if (comdata.find("ERROR")==-1):
                                continue
                       
        print("Sim7020c Start Succeed! \n")
        return

def connect_mqtt():
    print("connect new MQTT")
    time.sleep(60)
    comdata = ""
    ser.write("AT+CMQDISCON=0\r\n".encode('utf-8'))
    time.sleep(1)
    ser.write('AT+CMQNEW="182.92.56.252","61613",12000,100\r\n'.encode('utf-8'))
    while (comdata.find("OK")==-1):
                time.sleep(0.1)
                while (ser.inWaiting()>0):
                        comdata = ser.read(ser.inWaiting())
                        comdata = comdata.decode("ascii")
                        comdata = comdata.strip()
                        print(comdata)
def send_mqtt():
    comdata = ""
    ser.write('AT+CMQCON=0,3,"myclient",6000,0,0,"admin","password"\r\n'.encode('utf-8'))
    while (comdata.find("OK")==-1):
                time.sleep(0.1)
                while (ser.inWaiting()>0):
                        comdata = ser.read(ser.inWaiting())
                        comdata = comdata.decode("ascii")
                        comdata = comdata.strip()
                        print(comdata)
def send_topic(m,n):
    comdata = ""
    ser.write('AT+CMQPUB=0,"Monitor2",1,0,0,"{}","{}"\r\n'.format(m,n).encode('utf-8'))
    time.sleep(1)
    while (comdata.find("OK")==-1):
                time.sleep(0.1)
                while (ser.inWaiting()>0):
                        comdata = ser.read(ser.inWaiting())
                        comdata = comdata.decode("ascii")
                        comdata = comdata.strip()
                        print(comdata)

 
 
 
reboot()
connect_mqtt()
time.sleep(0.5)
send_mqtt()
time.sleep(0.5) 

        

    
    
    
    
    
    