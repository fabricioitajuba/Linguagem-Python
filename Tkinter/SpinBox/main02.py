# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#12/11/2020
#SpinBox
#para executar: $ python main02.py

from tkinter import *

def valorEscala():
	print("Valor da escala: " + str(sb_valores.get()))

app = Tk()
app.title("Scale")
app.geometry("500x300")

sb_valores = Spinbox(app, width=3, values=(1, 3, 5, 7, 9))
sb_valores.pack()

btn_valor = Button(app, text="Valor da ", command=valorEscala)
btn_valor.pack()

app.mainloop()