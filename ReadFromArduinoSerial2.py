import serial
import time

arduino = serial.Serial(port='/dev/ttyACM0',   baudrate=9600, timeout=.1)


def write_read(x):
    arduino.write(bytes(x,   'utf-8'))
    #arduino.write('0')
    time.sleep(0.1)
    data = arduino.readline()
    dataString=data.decode('utf-8')
    Ndata=dataString.rstrip()
    return   Ndata


while True:
    time.sleep(0.5)
    #value   = write_read("0")
    AdCmd=0
    value   = write_read(str(AdCmd))
    if(value):
        Ax=int(value)/1023*5
        print("data from Arduino:",Ax) 
    else: 
        print("no valid data")

