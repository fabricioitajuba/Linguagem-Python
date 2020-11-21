# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#21/11/2020
#ProgressBar
#para executar: $ python main02.py

from tkinter import *
from tkinter import ttk

var = 0

def valBarra():
	global var
	var = var+1
	varBarra.set(var)

form = Tk()
form.title("ProgressBar 1")
form.geometry("500x300")

#variável que irá alterar o valor da barra
varBarra = DoubleVar()
#varBarra.set(10)
varBarra.set(var)
#Cria a barra
pb = ttk.Progressbar(form, variable = varBarra, maximum = 100)
pb.place(x=0, y=0, width=500, height=40)#posicionamento e tamanho
#Cria o botão
btn=Button(form, text="Alterar o valor", command=valBarra)
btn.place(x=0, y=50, width=100, height=40)#posicionamento e tamanho

form.mainloop()