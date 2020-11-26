# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#25/11/2020
#Este programa abre um arquivo csv qualquer, mostra na tela e plota os dados
#para executar: $ python main.py

import serial
import serial.tools.list_ports	
from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from tkinter import Frame, Tk, BOTH, Text, Menu, END
import matplotlib.pyplot as plt
import csv


t = []
Xa = []
Xb = []
Xc = []

formPrincipal = Tk()


################################################################################
#Rotinas de comunicação

def get_ports():

    ports = serial.tools.list_ports.comports()
    
    return ports

def findModulo(portsFound):
    
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
	connectPort = findModulo(foundPorts)

	if connectPort != 'None':
	    ser = serial.Serial(connectPort,baudrate = 9600, timeout=1)
	    #print('Connected to ' + connectPort)
	    lb_conexao = Label(formPrincipal, text ="Conectado em: "+connectPort)
	else:
	    lb_conexao = Label(formPrincipal, text ="Equipamento não conectado!")
	
	lb_conexao.place(x=10, y=10)


#################################################################################
#Rotina para plotar o gráfico

def formPlotar():

	plt.plot(t,Xa, label='Xa')
	plt.plot(t,Xb, label='Xb')
	plt.plot(t,Xc, label='Xc')
	plt.xlabel('Tempo [ms]', fontweight="bold")
	plt.ylabel('Estado [Desligado/Ligado]', fontweight="bold")
	plt.title('Tempo de fechamento\ndo disjuntor', fontweight="bold")
	plt.legend()
	plt.grid()
	plt.show()

################################################################################
#Rotina para carregar os dados

def formAbrir():

	#onOpen()
	ftypes = [('Arquivos csv', '*.csv'), ('All files', '*')]

	dlg = tkinter.filedialog.Open(formPrincipal, filetypes=ftypes)
	fl = dlg.show()
	
	tv = ttk.Treeview(formPrincipal, columns=('A', 'B', 'C', 'D'), show='headings')

	tv.column('A', minwidth=0, width=50)
	tv.column('B', minwidth=0, width=50)
	tv.column('C', minwidth=0, width=50)
	tv.column('D', minwidth=0, width=50)

	tv.heading('A', text='t [ms]')
	tv.heading('B', text='Xa')
	tv.heading('D', text='Xc')

	#tv.pack()
	tv.place(x=10, y=50)


	n=0

	with open(fl,'r') as csvfile:
	    plots = csv.reader(csvfile, delimiter=';')
	    for row in plots:
	        t.append(float(row[0]))
	        Xa.append(int(row[1]))
	        Xb.append(int(row[2]))
	        Xc.append(int(row[3]))
	        n += 1

	for i in range(n):
		tv.insert("", "end", values=(t[i], Xa[i], Xb[i], Xc[i]))

	btn_plota = Button(formPrincipal, text="Plotar", width=5, command=formPlotar)
	btn_plota.place(x=10, y=280)

################################################################################
#Rotina principal

#Criação do menu
menubar = Menu(formPrincipal)
#Menu Arquivo
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Abrir", command=formAbrir)
filemenu.add_separator()
filemenu.add_command(label="Sair", command=formPrincipal.quit)
menubar.add_cascade(label="Arquivo", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
#editmenu.add_command(label="Configurar porta", command=porta)
editmenu.add_command(label="Conectar", command=formConectar)
menubar.add_cascade(label="Conexão", menu=editmenu)

formPrincipal.config(menu=menubar)

formPrincipal.geometry("750x450+100+100")
formPrincipal.resizable(False, False)
formPrincipal.title("Gera plota 03")

formPrincipal.mainloop()