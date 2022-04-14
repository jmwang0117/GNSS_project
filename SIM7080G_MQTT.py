#!/usr/bin/python

import RPi.GPIO as GPIO
import serial
import time

ser = serial.Serial('/dev/ttyUSB0',115200)

ser.flushInput()

powerKey = 4
rec_buff = ''
Message = 'www.waveshare.com'

def powerOn(powerKey):
        print('SIM7080X is starting:')
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(powerKey,GPIO.OUT)
        time.sleep(0.1)
        GPIO.output(powerKey,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(powerKey,GPIO.LOW)
        time.sleep(5)
        ser.flushInput()

def powerDown(powerKey):
        print('SIM7080X is loging off:')
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(powerKey,GPIO.OUT)
        GPIO.output(powerKey,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(powerKey,GPIO.LOW)
        time.sleep(5)
        print('Good bye')


def sendAt(command,back,timeout):
    rec_buff = ''
    ser.write((command+'\r\n').encode())
    time.sleep(timeout)
    if ser.inWaiting():
        time.sleep(1)
        rec_buff = ser.read(ser.inWaiting())
    if rec_buff != '':
        if back not in rec_buff.decode():
            print(command + ' back:\t' + rec_buff.decode())
            return 0
        else:
            print(rec_buff.decode())
            return 1
    else:
        print(command + ' no responce')

def checkStart():
    while True:
        # simcom module uart may be fool,so it is better to send much times when it starts.
        ser.write('AT\r\n'.encode())
        time.sleep(1)
        ser.write('AT\r\n'.encode())
        time.sleep(1)
        ser.write('AT\r\n'.encode())
        time.sleep(1)
        if ser.inWaiting():
            time.sleep(0.01)
            recBuff = ser.read(ser.inWaiting())
            print('SIM7080X is ready\r\n')
            print( 'try to start\r\n' + recBuff.decode() )
            if 'OK' in recBuff.decode():
                recBuff = ''
                break 
        else:
            powerOn(powerKey)

try:
    checkStart()
    print('wait for signal')                       
    time.sleep(1)
    
    #ser.write((command+'\r\n').encode())
    #sendAt('AT+CNACT=0,0', 'OK', 1)
    #sendAt('AT+CSQ','OK',1)
    #sendAt('AT+CPSI?','OK',1)
    #sendAt('AT+CGREG?','+CGREG: 0,1',0.5)
    sendAt('AT+CNACT=0,1','OK',1)
    sendAt('AT+CNACT?','OK',1)
    #sendAt('AT+CACID=0','OK',1)
    ser.write('AT+SMCONF="URL","182.92.56.252","61613"\r\n'.encode('utf-8'))
    time.sleep(0.5)
    ser.write('AT+SMCONF="USERNAME","admin"\r\n'.encode('utf-8'))
    time.sleep(0.5)
    ser.write('AT+SMCONF="PASSWORD","password"\r\n'.encode('utf-8'))
    time.sleep(0.5)
    ser.write('AT+SMCONF="KEEPTIME",60\r\n'.encode('utf-8'))
    time.sleep(0.5)
    ser.write('AT+SMCONF="CLIENTID","id"\r\n'.encode('utf-8'))
    time.sleep(0.5)
    ser.write('AT+SMCONN\r\n'.encode('utf-8'))
    time.sleep(0.5)
    
    
    '''
    sendAt('AT+SMCONF=\"URL\",\"182.92.56.252\",\"61613\"','OK',1)
    sendAt('AT+SMCONF=\"USERNAME\",\"admin\"','OK',1)
    sendAt('AT+SMCONF=\"PASSWORD\",\"password\"','OK',1)
    sendAt('AT+SMCONF=\"KEEPTIME\",60','OK',1)
    sendAt('AT+SMCONF=\"CLIENTID\",\"id\"','OK',1)
    sendAt('AT+SMCONN','OK',5)
    '''
    time.sleep(5)
    #sendAt('AT+SMSUB=\"waveshare_pub\",1','OK',1)
    while True:
        sendAt('AT+SMPUB=\"waveshare_sub\",17,1,0','OK',1)
        ser.write(Message.encode())
        time.sleep(1);
        print('send message successfully!')
    #sendAt('AT+SMDISC','OK',1)

    #powerDown(powerKey)
except:
    if ser != None:
        ser.close()
    powerDown(powerKey)
    GPIO.cleanup()
