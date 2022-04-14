#coding=utf-8
import serial
import time
import os,sys
import binascii
import datetime
#from BDSMQTT1 import send_topic
ser3 = serial.Serial("/dev/ttyS0",9600)

def hex2dec(string_num): 
          return int(string_num.upper(), 16)

def rain():
    ser1 = serial.Serial("/dev/ttyUSB0",9600)
    myinput1 = bytes.fromhex('01 03 01 05 00 01 95 F7')
    ser1.write(myinput1)
    time.sleep(0.5)
    s1 = ser1.inWaiting()
    if s1!=0:
        data1 = str(binascii.b2a_hex(ser1.read(s1)))[2:-1]
        print(data1)
            
        return data1
def soil():
    ser2 = serial.Serial("/dev/ttyUSB1",9600)
    myinput2 = bytearray.fromhex('01 03 00 02 00 01 25 CA')
    ser2.write(myinput2)
    time.sleep(0.5)
    s2 = ser2.inWaiting()
    if s2!=0:
        data2 = str(binascii.b2a_hex(ser2.read(s2)))[2:-1]
        
        print(data2)
        return data2

while True:
    
    now = datetime.datetime.now()
    Time_Year = str(now.year)
    Time_Month = str(now.month)
    Time_Day = str(now.day)
    Time_Hour = str(now.hour)
    Time_Minute = str(now.minute)
    Time_Second = str(now.second)
    #雨量
    
    rain1 = rain()
    rain_data = hex2dec(rain1[6:10])/10
    print(rain_data)
    mon1_rain =  str(6)+ '/'+str(26) 
    Time_All = '/' + Time_Year + '/' +Time_Month+ '/' + Time_Day+ '/' + Time_Hour+ '/' + Time_Minute+ '/' + Time_Second + '/' 
    rain_data = str(rain_data)  + '/' + str('Nothing')
    rain_message = mon1_rain + Time_All + rain_data
    ser3.write((rain_message+'\r\n').encode('utf-8'))
    
 
    #土壤湿度
    soil1 = soil()
    soil_data = hex2dec(soil1[6:10])/10
    print(soil_data)
    mon1_soil =  str(7)+ '/'+str(27) 
    Time_All = '/' + Time_Year + '/' +Time_Month+ '/' + Time_Day+ '/' + Time_Hour+ '/' + Time_Minute+ '/' + Time_Second + '/' 
    soil_data = str(soil_data)  + '/' + str('Nothing')
    soil_message = mon1_soil + Time_All + soil_data
    ser3.write((soil_message+'\r\n').encode('utf-8'))
    
    
    
    
    
        
     
   