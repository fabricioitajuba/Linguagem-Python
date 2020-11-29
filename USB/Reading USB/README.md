# Neste exemplo, iremos ler o mouse que está conectado na porta usb
lsusb - mostra os dispositivo conectados na port usb

Ex: o Mouse está conectado:

$ lsusb

Bus 004 Device 005: ID 1bcf:0005 Sunplus Innovation Technology Inc. Optical Mouse

Para saber informações mais específicas:

$ lsusb -D /dev/bus/usb/004/005

Precisamos das seguintes informações:


idVendor           0x1bcf Sunplus Innovation Technology Inc.

idProduct          0x0005 Optical Mouse

iremos utilizar o pyusb que pode ser instalado:

pip install pyusb 

ou

pip3 install pyusb

para executar: 

**sudo python3 main.py

se não reconhecer o "usb.core", instale o seguinte pacote:

sudo apt-get install python-usb python3-usb

Execute o programa e mexa no mouse logo em seguida
