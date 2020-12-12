# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#12/11/2020
#Scale
#para executar: $ python main01.py

from tkinter import *

def valorEscala():
	print("Valor da escala: " + str(sc_escala.get()))

app = Tk()
app.title("Scale")
app.geometry("500x300")

lb_valor = Label(app, text="Valor")
lb_valor.pack()

sc_escala = Scale(app, from_=0, to=100, orient=HORIZONTAL)
sc_escala.set(50)
sc_escala.pack()

btn_valor = Button(app, text="Valor da escala", command=valorEscala)
btn_valor.pack()

app.mainloop()