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
    return   data


while True:
    num = input("Enter a number: ")
    value   = int(write_read(num))
    print("data from Arduino:", value*100)
    #print("data from Arduino INT:",int(value))

