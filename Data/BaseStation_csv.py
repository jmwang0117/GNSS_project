# encoding:UTF-8
import serial
import pandas as pd
import datetime as t
import time
ser = serial.Serial("/dev/ttyACM0",9600)

          
           
add_time = []
            
lat_add = []
    
lon_add = []
            
alt_add = []
            
num_add = []
            
vdop_add = []
        
hdop_add = []
            
pdop_add = []

# f = open("test.txt",'a')
while True:
    line1 = str(ser.readline().decode().strip())
    print(line1)
    line2 = str(ser.readline().decode().strip())
    print(line2)
    if line1.startswith('$GPGSA'):
        
        line1 = str(line1).split(',')
        pdop = float(line1[15])
        hdop = float(line1[16])
        vdop123 = line1[17]
        vdop = float(vdop123[0:3])
        vdop_add.append(vdop)
        pdop_add.append(pdop)
        hdop_add.append(hdop)
        print("PDOP:", pdop)
        print("HDOP:", hdop)
        print("VDOP:", vdop)

    if line2.startswith('#BESTPOSA'):
        
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
        tt = t.datetime.now().time()
        add_time = []
        add_time.append(tt)
        save = {"time":add_time,"latitude":lat_add,"longitude":lon_add,"altitude":alt_add,'state_num':num_add,"VDOP":vdop_add,"HDOP":hdop_add,"PDOP":pdop_add}
        dataframe = pd.DataFrame.from_dict(save,orient='index')
        dataframe = dataframe.transpose()
        dataframe.to_csv("GNSS-RTK_BaseStation.csv", index=False, mode='a', header=False, sep=',',)
        time.sleep(2)
    # f.write(str(distance_geopy))
    # f.write(str(" "))
    # f.write(str(height_add))
    # f.write("\n")
   



