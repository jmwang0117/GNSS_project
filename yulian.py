import serial
import time
import binascii
ser = serial.Serial("/dev/ttyUSB0",9600)
while True:

    myinput = bytes.fromhex('01 03 01 05 00 01 95 f7')
    ser.write(myinput)
    time.sleep(2)
    s = ser.inWaiting()
    if s!=0:
        data = str(binascii.b2a_hex(ser.read(s)))[2:-1]
        print(data[6:10])
    
ser.flushInput()