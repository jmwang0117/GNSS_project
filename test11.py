#encoding:UTF-8
import serial #导入serial模块
import time
import L76X
import math
import datetime
import pandas as pd
number = '$PMTK353,1,0,0,0,1'
x=L76X.L76X()
x.L76X_Set_Baudrate(9600)
x.L76X_Send_Command(x.SET_NMEA_BAUDRATE_115200)
    #x.L76X_Send_Command(SET_NAME)
time.sleep(2)
x.L76X_Set_Baudrate(115200)
x.L76X_Send_Command(x.SET_POS_FIX_400MS);
    #Set output message
x.L76X_Send_Command(x.SET_NMEA_OUTPUT);
x.L76X_Exit_BackupMode();
x.L76X_Send_Command(number)
ser = serial.Serial("/dev/ttyS0",115200)
time1 = []
time2 = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
listpdop = []
listvdop = []
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
        listvdop.append(vdop)
        listpdop.append(pdop)
        print "PDOP:",pdop
        print "HDOP:",hdop
        print "VDOP:",vdop
        time.sleep(5)
        
    if line.startswith('$GNGGA'):
            #print('data：' + str(line))
            line = str(line).split(',')  # 将line以“，”为分隔符
            jing = float(line[4][:3]) + float(line[4][3:])/60
            # 读取第5个字符串信息，从0-2为经度，即经度为116，再加上后面的一串除60将分转化为度
            wei = float(line[2][:2]) + float(line[2][2:])/60
            # 纬度同理
            number = int(line[7])
            hdop = float(line[8])
            height = float(line[9])
            a = datetime.datetime.now().date()
            b = datetime.datetime.now().time()
            time1.append(a)
            time2.append(b)
            list1.append(jing)
            list2.append(wei)
            list3.append(number)
            list4.append(hdop)
            list5.append(height)
            dataframe = pd.DataFrame({'VDOP':listvdop,'PDOP':listpdop,'Year':time1,'Time':time2,'Longitude':list1,'Latitude':list2,'number':list3,'HDOP':list4,'Altitude':list5})
            dataframe.to_csv(r"GNSS_0402_0.csv",index=False,sep=',')
            print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
            print "Lon:",jing
            print "Lat:",wei
            print "height:",height
            print "HDOP:",hdop
            print "number:",number
            time.sleep(5)
