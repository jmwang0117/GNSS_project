import serial
ser = serial.Serial("/dev/ttyACM0",9600)
f = open("rover_GPS.txt",'a')
while True:
    line1 = str(ser.readline().decode().strip())
    line2 = str(ser.readline().decode().strip())
    if line1.startswith('$GPGSA'):
            print(line1)
            f.write(line1) 
            f.write("\n")   
    if line2.startswith('#BESTPOSA'):
            print(line2)
            f.write(line2) 
            f.write("\n")   
