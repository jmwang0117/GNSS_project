import serial
import time
import binascii
ser = serial.Serial("/dev/ttyUSB0",9600)
def hex_dec(str2): #十六转十                                                                                                                       
    b = eval(str2)                                                                                                                             
    print('十六进制： %s 转换成十进制为：%s:' %(str2,b))                                                                                                   
    return b

while True:

    myinput = bytes.fromhex('01 03 00 02 00 01 25 CA')
    ser.write(myinput)
    time.sleep(2)
    s = ser.inWaiting()
    if s!=0:
        data = str(binascii.b2a_hex(ser.read(s)))[2:-1]
        print(data)
        data1 = '0x'+data[8:10]
        tu = hex_dec(data1)/10
        print(tu)
    
ser.flushInput()
