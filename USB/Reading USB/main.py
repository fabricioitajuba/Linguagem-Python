# Eng. Fabricio de Lima Ribeiro
# 29/11/2020
# Neste exemplo, iremos ler o mouse que está conectado
# para executar: sudo python3 main.py

import usb.core

dev = usb.core.find(idVendor = 0x1bcf, idProduct = 0x0005)
ep = dev[0].interfaces()[0].endpoints()[0]
i = dev[0].interfaces()[0].bInterfaceNumber
dev.reset()

if dev.is_kernel_driver_active(i):
	dev.detach_kernel_driver(i)

dev.set_configuration()
eaddr = ep.bEndpointAddress

r = dev.read(eaddr, 1024)
print(len(r))