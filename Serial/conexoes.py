#Eng. Fabricio de Lima Ribeiro
#Este programa encontra as conecxoes ativas
#25/11/20


import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())

for p in ports:
    print p





    

