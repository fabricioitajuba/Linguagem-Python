# Este dispositivo verifica se um dispositivo está ou não
# conectado na usb
# 30/11/2020
# Fabrício de Lima Ribeiro
# Ex:
# $ lsusb
# Bus 003 Device 002: ID 275d:0ba6  USB OPTICAL MOUSE

import usb.core
import usb.util

# find our device
dev = usb.core.find(idVendor=0x275d, idProduct=0x0ba6)

# was it found?
if dev is None:
    raise ValueError('Device not found')
else:
	print("Dispositivo encontrado!")
