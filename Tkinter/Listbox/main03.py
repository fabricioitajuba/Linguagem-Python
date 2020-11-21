# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#21/11/2020
#Listbox
#para executar: $ python main03.py

def imprimirEsporte():
	print("Esporte: " + str(lb_esportes.get(ACTIVE)))

def adicionarEsporte():
	lb_esportes.insert(END, novoesporte.get())

from tkinter import *

form = Tk()
form.title("Listbox")
form.geometry("500x300")

listaEsportes=["Futebol", "Vôlei", "Basquete"]

lb_esportes=Listbox(form)
for esportes in listaEsportes:
	lb_esportes.insert(END, esportes)
lb_esportes.pack()

btn_esporte=Button(form, text="Imprimir esporte", command=imprimirEsporte)
btn_esporte.pack()


novoesporte=Entry(form)
novoesporte.pack()

btn_inseriresporte=Button(form, text="Adicionar esporte", command=adicionarEsporte)
btn_inseriresporte.pack()

mainloop()