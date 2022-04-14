#encoding:UTF-8
from geopy import distance
from math import sin, cos, sqrt, atan2, radians
import serial
import pandas as pd
import datetime as t
import time
ser = serial.Serial("/dev/ttyACM1",9600)
ser1 = serial.Serial("/dev/ttyUSB0",9600)
add_time = []
            
lat_add = []
    
lon_add = []
            
alt_add = []
            
num_add = []
            
vdop_add = []
        
hdop_add = []
            
pdop_add = []

shuiping_add = []

chuizhi_add  = []
# f = open("test.txt",'a')
while True:
    line1 = str(ser.readline().decode().strip())
    print(line1)
    line2 = str(ser.readline().decode().strip())
    print(line2)
    if line1.startswith('$GPGSA'):
            print(line1)
            line1 = str(line1).split(',')
            pdop  = float(line1[15])
            hdop = float(line1[16])
            vdop123 = line1[17]
            vdop = float(vdop123[0:3])
            vdop_add.append(vdop)
            pdop_add.append(pdop)
            hdop_add.append(hdop)
            print ("PDOP:",pdop)
            print ("HDOP:",hdop)
            print ("VDOP:",vdop)
            


    if line2.startswith('#BESTPOSA'):
            print(line2)
            samp = line2.split(";")
            Rover = samp[1].split(',')
            latitude = float(Rover[2])
            longitude = float(Rover[3])
            altitude = float(Rover[4])
            state_num = float(Rover[14])
            lat_add.append(latitude)
            lon_add.append(longitude)
            alt_add.append(altitude)
            num_add.append(state_num)
            print("latitude:",latitude)
            print("longitude:",longitude)
            print("altitude:",altitude)
            print("state_num:",state_num)
            
            base_height = 1576.6132     #基准站高度
            base_latitude =36.10363098447    #基准站纬度
            base_longitude = 103.72104383483     #基准站经度
            lat1, lon1, lat2, lon2, R = base_latitude,base_longitude,latitude,longitude, 6373.0
            coordinates_from = [lat1, lon1]
            coordinates_to = [lat2, lon2]
            dlon = radians(lon2) - radians(lon1)
            dlat = radians(lat2) - radians(lat1)
            a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            distance_geopy = distance.distance(coordinates_from, coordinates_to).m*1000 #水平位移
            distance_geopy = round(distance_geopy,4)
            height_add = altitude - base_height     #高程位移
            height_add = round(height_add*1000,4)
            print('distance using geopy: ',distance_geopy)
            print('height: ',height_add)
            shuiping_add.append(distance_geopy)
            chuizhi_add.append(height_add)
            
            tt = t.datetime.now()
            add_time = []
            add_time.append(tt)
            # f.write(str(distance_geopy))
            # f.write(str(" "))
            # f.write(str(height_add))
            # f.write("\n")
            '''
            
            save = {"time":add_time,"Horizontal":shuiping_add,"vertical":chuizhi_add,"latitude":lat_add,"longitude":lon_add,"altitude":alt_add,'state_num':num_add,"VDOP":vdop_add,"HDOP":hdop_add,"PDOP":pdop_add}
            dataframe = pd.DataFrame.from_dict(save,orient='index')
            dataframe = dataframe.transpose()
            dataframe.to_csv("GNSS-RTK_RoverStation.csv", index=False, mode='a', header=False, sep=',',)
            '''
            
            #Time
            Time_Year = str(tt.year)
            Time_Month = str(tt.month)
            Time_Day = str(tt.day)
            Time_Hour = str(tt.hour)
            Time_Minute = str(tt.minute)
            Time_Second = str(tt.second)
            
            #distance_shuiping
            distance_ipv6 =  str(15)+ '/'+str(37) 
            Time_All = '/' + Time_Year + '/' +Time_Month+ '/' + Time_Day+ '/' + Time_Hour+ '/' + Time_Minute+ '/' + Time_Second + '/' 
            distance_geopy_data = str(distance_geopy)  + '/' + str('Nothing')+'\r\n'
            distance_geopy_data_message = distance_ipv6 + Time_All + distance_geopy_data
            print (distance_geopy_data_message)
            ser1.write((distance_geopy_data_message).encode('utf-8'))
            time.sleep(0.5)
            
            #distance height
            height_distance_ipv6 =  str(15)+ '/'+str(38) 
            Time_All = '/' + Time_Year + '/' +Time_Month+ '/' + Time_Day+ '/' + Time_Hour+ '/' + Time_Minute+ '/' + Time_Second + '/' 
            height_distance_data = str(height_add)  + '/' + str('Nothing')+'\r\n'
            height_distance_data_message = height_distance_ipv6 + Time_All + height_distance_data
            print (height_distance_data_message)
            ser1.write((height_distance_data_message).encode('utf-8'))
            time.sleep(0.5)
             
        
        
        
  