# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#26/11/2020
#Este programa verifica se o arduino está conectado ou não
#para executar: $ python main.py

import serial
import serial.tools.list_ports	
from tkinter import *


def get_ports():

    ports = serial.tools.list_ports.comports()
    
    return ports

def findArduino(portsFound):
    
    commPort = 'None'
    numConnection = len(portsFound)
    
    for i in range(0,numConnection):
        port = portsFound[i]
        strPort = str(port)
        
        splitPort = strPort.split(' ')
        commPort = (splitPort[0])

    return commPort


def formConectar(): 

	foundPorts = get_ports()        
	connectPort = findArduino(foundPorts)

	if connectPort != 'None':
	    ser = serial.Serial(connectPort,baudrate = 9600, timeout=1)
	    #print('Connected to ' + connectPort)
	    lb_conexao = Label(formPrincipal, text ="Conectado em: "+connectPort)
	else:
	    lb_conexao = Label(formPrincipal, text ="Equipamento não conectado!")
	
	lb_conexao.place(x=10, y=20)


formPrincipal = Tk()

#Criação do menu
menubar = Menu(formPrincipal)
#Menu Arquivo
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Sair", command=formPrincipal.quit)
menubar.add_cascade(label="Arquivo", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
#editmenu.add_command(label="Configurar porta", command=porta)
editmenu.add_command(label="Conectar", command=formConectar)
menubar.add_cascade(label="Conexão", menu=editmenu)

formPrincipal.config(menu=menubar)

formPrincipal.geometry("750x450+100+100")
formPrincipal.resizable(False, False)
formPrincipal.title("Encontra o arduino")

formPrincipal.mainloop()