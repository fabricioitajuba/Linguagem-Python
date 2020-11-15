import serial
import time

ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
time.sleep(3)
numPoints = 5
dataList = [0]*numPoints
dataFile = open('dataFile.txt', 'w') #copia os dados para um arquivo

def getValues():
	ser.write(b'g')
	arduinoData = ser.readline().decode().split('\r\n')
	return arduinoData[0]

while 1:
    
    userInput = input('Get data point?')

    if userInput == 'y':
    	for i in range(0,numPoints):
    		data = getValues()
    		dataFile.write(data + ' ') #salva os dados no arquivo
    		data = int(data) #sem essa linha recebe uma string
    		dataList[i] = data

    	dataAvg = sum(dataList)/numPoints  #calcula a média
    	print(dataAvg)
    	print(dataList)

    	dataFile.close() #fecha o arquivo
    	break