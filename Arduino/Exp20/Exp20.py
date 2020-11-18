import serial
import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def getSerialData(self, Samples, serialConnection, lines, lineValueText, lineLabel):
	value = float(serialConnection.readline().strip())
	data.append(value)
	lines.set_data(range(Samples), data)
	lineValueText.set_text(lineLabel+' = ' + str(round(value, 2)))

serialPort = '/dev/ttyACM0'
baudRate = 9600

try:
	serialConnection = serial.Serial(serialPort, baudRate, timeout = 1)
	time.sleep(3)
except:
	print('Cannot conect to the port')

Samples = 100
data = collections.deque([0] * Samples, maxlen = Samples)
sampleTime = 100

xmin = 0
xmax = Samples
ymin = 0
ymax = 6

fig = plt.figure(figsize=(13,6))
ax = plt.axes(xlim = (xmin, xmax), ylim = (ymin, ymax))
plt.title("Real-time Sensor reading")
ax.set_xlabel("Samples")
ax.set_ylabel("Voltage value")

lineLabel = 'Voltage'
lines = ax.plot([], [], label = lineLabel)[0]
lineValueText = ax.text(0.85, 0.95, '', transform = ax.transAxes)

anim = animation.FuncAnimation(fig, getSerialData, fargs = (Samples, serialConnection, lines, lineValueText, lineLabel), interval = sampleTime)
plt.show()

serialConnection.close()