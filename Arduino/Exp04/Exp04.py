import serial
import time

ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
time.sleep(3)
numPoints = 10
dataList = [0]*numPoints
dataFile = open('dataFile.txt', 'w') #copia os dados para um arquivo
numRowsCollect = 50


def getValues():

	ser.write(b'g')
	arduinoData = ser.readline().decode().split('\r\n')
	return arduinoData[0]

def printToFile(data, index):

	dataFile.write(data)
	if index != (numPoints - 1):
		dataFile.write(',')
	else:
		dataFile.write('\n')

def getAverage(dataSet, row):
	
	dataAvg = sum(dataSet) / len(dataSet)
	print('Average for ' + str (row) + ' is: ' + str(dataAvg))

while (1):
    
    userInput = input('Get data point?')

    if userInput == 'y':
    	for row in range(0,numRowsCollect):
	    	for i in range(0,numPoints):
	    		data = getValues()
	    		printToFile(data, i)
	    		dataInt = int(data)
	    		dataList[i] = dataInt

	    	getAverage(dataList, row)

    	dataFile.close() #fecha o arquivo
    	break