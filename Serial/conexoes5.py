# -*- coding: utf-8 -*-
#Fabricio de Lima Ribeiro
#28/11/2020
#Este programa acha as conexões ativas no computador e retorna em um ComboBox
#25/11/20

import sys
import glob
import serial
from tkinter import *
from tkinter import ttk


if sys.platform.startswith('win'):
    ports = ['COM%s' % (i + 1) for i in range(256)]
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
    # this excludes your current terminal "/dev/tty"
    ports = glob.glob('/dev/tty[A-Za-z]*')
elif sys.platform.startswith('darwin'):
    ports = glob.glob('/dev/tty.*')
else:
    raise EnvironmentError('Unsupported platform')

result = []
for port in ports:
    try:
        s = serial.Serial(port)
        s.close()
        result.append(port)
    except (OSError, serial.SerialException):
        pass


################################################################################
# Trata conexão
def serial_ports():
	print('teste')


################################################################################
# Form conexão

formConexao = Tk()

formConexao.geometry("350x150+200+200")
formConexao.resizable(False, False)
formConexao.title("Conexões disponíveis...")

if len(result) > 0:
	lb_conexao = Label(formConexao, text ="Conexões disponíveis:")
	lb_conexao.pack()

	cb_conexao = ttk.Combobox(formConexao, values = result)
	cb_conexao.pack()

	btn_conexao = Button(formConexao, text="Conectar", width=5, command=serial_ports)
	btn_conexao.pack()
else:
	lb_conexao = Label(formConexao, text ="Nenhuma conexão disponível!")
	lb_conexao.pack()

formConexao.mainloop()