#encoding:UTF-8
import serial #导入serial模块
import time
import L76X
import math
import datetime
import binascii
import pynmea2
import os

#from MQTT import send_topic
number = '$PMTK353,1,0,0,0,1'
x=L76X.L76X()
x.L76X_Set_Baudrate(9600)
x.L76X_Send_Command(x.SET_NMEA_BAUDRATE_115200)
    #x.L76X_Send_Command(SET_NAME)
time.sleep(1)
x.L76X_Set_Baudrate(115200)
x.L76X_Send_Command(x.SET_POS_FIX_400MS);
    #Set output message
x.L76X_Send_Command(x.SET_NMEA_OUTPUT);
x.L76X_Exit_BackupMode();
x.L76X_Send_Command(number)
ser = serial.Serial("/dev/USB3",115200)
ser1 = serial.Serial("/dev/USB4",115200)
 

    
while True:
    line = str(ser.readline())
    line1 = str(ser.readline())
    print(line)
    print(line1)
    
    if line1.startswith('$GPGSA'):
        line1 = str(line1).split(',')
        pdop  = float(line1[15])
        hdop = float(line1[16])
        vdop1 = line1[17]
        vdop = float(vdop1[0:4])
        print "PDOP:",pdop
        print "HDOP:",hdop
        print "VDOP:",vdop
        '''
        mqtt_15 = "15/"+str(vdop) +"/"+str(hdop)+"/"+str(pdop)
        len_1 = len(mqtt_15)
        send_topic(len_1,mqtt_15)
        '''
    if line.startswith('$GNGGA'):
            record = pynmea2.parse(line)
            jing = record.longitude
            wei = record.latitude
            height = record.altitude
            number = record.num_sats
            
            now = datetime.datetime.now()
            Time_Year = str(now.year)
            Time_Month = str(now.month)
            Time_Day = str(now.day)
            Time_Hour = str(now.hour)
            Time_Minute = str(now.minute)
            Time_Second = str(now.second)
            Ref_lat =  str(1)+ '/'+str(1) 
            Time_All = '/' + Time_Year + '/' +Time_Month+ '/' + Time_Day+ '/' + Time_Hour+ '/' + Time_Minute+ '/' + Time_Second + '/' 
            lat_data = str(wei)  + '/' + str('Nothing')+'\r\n'
            lat_message = Ref_lat + Time_All + lat_data
            #len_lat = len(lat_message)
            #send_topic(len_lat,lat_message)
            print lat_message
            ser1.write((lat_message).encode('utf-8'))
            time.sleep(0.5)
            Ref_lon = str(1)+ '/'+str(2) 
            lon_data = str(jing) + '/' + str('Nothing')+'\r\n'
            lon_message = Ref_lon + Time_All + lon_data
            #len_lon = len(lon_message)
            #send_topic(len_lon,lon_message)
            print lon_message
            ser1.write((lon_message).encode('utf-8'))
            time.sleep(0.5)
            Ref_alt = str(1)+ '/'+str(3) 
            alt_data = str(height) + '/' + str('Nothing')+'\r\n'
            alt_message = Ref_alt + Time_All + alt_data
            #len_alt = len(alt_message)
            #send_topic(len_alt,alt_message)
            print alt_message
            ser1.write((alt_message).encode('utf-8'))
            time.sleep(0.5)
            Ref_num = str(1)+ '/'+str(4) 
            num_data = str(number) + '/' + str('Nothing')+'\r\n'
            num_message = Ref_num + Time_All + num_data
            #len_num = len(num_message)
            #send_topic(len_num,num_message)
            print num_message
            ser1.write((num_message).encode('utf-8'))
            time.sleep(0.5)
            Ref_vdop = str(1)+ '/'+str(5) 
            vdop_data = str(vdop) + '/' + str('Nothing')+'\r\n'
            vdop_message = Ref_vdop + Time_All + vdop_data
            #len_vdop = len(vdop_message)
            #send_topic(len_vdop,vdop_message)
            print vdop_message
            ser1.write((vdop_message).encode('utf-8'))
            time.sleep(0.5)
            Ref_hdop = str(1)+ '/'+str(6) 
            hdop_data = str(hdop) + '/' + str('Nothing')+'\r\n'
            hdop_message = Ref_hdop + Time_All + hdop_data
            #len_hdop = len(hdop_message)
            #send_topic(len_hdop,hdop_message)
            print hdop_message
            ser1.write((hdop_message).encode('utf-8'))
            time.sleep(0.5)
            Ref_pdop = str(1)+ '/'+str(7) 
            pdop_data = str(pdop) + '/' + str('Nothing')+'\r\n'
            pdop_message = Ref_pdop + Time_All + pdop_data
            #len_pdop = len(pdop_message)
            #send_topic(len_pdop,pdop_message)
            print pdop_message
            
            ser1.write((pdop_message).encode('utf-8'))
            time.sleep(0.5)
            
          
            
            
       
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                     
            
            
           
