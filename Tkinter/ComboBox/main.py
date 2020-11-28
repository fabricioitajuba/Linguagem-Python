# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#28/11/2020
#ComboBox
#para executar: $ python main.py

from tkinter import *
from tkinter import ttk

def imprimirEsporte():
	ve = cb_esportes.get()
	print("Esporte "+ve)

form = Tk()
form.title("ComboBox")
form.geometry("500x300")

listEsportes = ["Futebol", "Vôlei", "Basquete"]

lb_esportes = Label(form, text="Esportes")
lb_esportes.pack()

cb_esportes = ttk.Combobox(form, values = listEsportes)
cb_esportes.set("Futebol")#Configura o valor inicial da lista (opcional)
cb_esportes.pack()

btn_esporte = Button(form, text = "Esporte selecionado", command = imprimirEsporte)
btn_esporte.pack()

form.mainloop()