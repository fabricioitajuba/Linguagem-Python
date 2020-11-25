#Eng. Fabricio de Lima Ribeiro
#Este programa encontra as conecxoes ativas e conecta automaticamente
#25/11/20

import serial
import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())

for p in ports:
    print p

con = str(p)

conn = con.split(" ")

print(conn[0])

ser = serial.Serial(conn[0], baudrate=9600, timeout=1)

while 1:
    #arduinoData = ser.readline()
    arduinoData = ser.readline().strip()
    print(arduinoData)