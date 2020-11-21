# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#21/11/2020
#Listbox
#para executar: $ python main02.py

from tkinter import *

form = Tk()
form.title("Listbox")
form.geometry("500x300")

listaEsportes=["Futebol", "Vôlei", "Basquete"]

lb_esportes=Listbox(form)
for esportes in listaEsportes:
	lb_esportes.insert(END, esportes)

lb_esportes.pack()

mainloop()