# -*- coding: utf-8 -*-
#Fabricio de Lima Ribeiro
#12/11/2020
#Exemplo de uso do OptionMenu
#para executar: $ python3 main.py

from tkinter import *

def imprimir_componente():
	cp = vcomponentes.get()
	print(cp)

form = Tk()
form.title("Exemplo de uso do OptionMenu")
form.geometry("500x300")

componentes = ["Resistor", "Capacitor", "Indutor"]

vcomponentes = StringVar()
vcomponentes.set(componentes[1])

op_componentes = OptionMenu(form, vcomponentes, *componentes)
op_componentes.pack()

botao = Button(form, text = "Imprimir", command = imprimir_componente)
botao.pack()

form.mainloop()