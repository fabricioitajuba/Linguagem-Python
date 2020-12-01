#Leitura de bytes pela serial e guarda em um arquivo csv
#01/12/20

import serial
import time
import csv

ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
ser.flushInput()

time.sleep(3)
ser.write(b'g')

while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
        with open("test_data.csv","a") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow([time.time(),decoded_bytes])
    except:
        print("Keyboard Interrupt")
        break