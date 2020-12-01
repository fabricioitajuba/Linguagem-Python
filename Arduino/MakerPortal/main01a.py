#Leitura de bytes pela serial
#01/12/20

import serial
import time

ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
ser.flushInput()

time.sleep(3)
ser.write(b'g')

while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = int(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
    except:
        print("Keyboard Interrupt")
        break