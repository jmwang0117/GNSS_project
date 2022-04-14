import serial
ser = serial.Serial("/dev/ttyACM1",9600)
f = open("BaseStation.txt",'a')
while True:
    line1 = str(ser.readline().decode().strip())
    print(line1)
    f.write(line1) 
    f.write("\n")   
