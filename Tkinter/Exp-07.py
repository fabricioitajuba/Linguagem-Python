# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#14/11/2020
#Processamento de dados
#para executar: $ python3 Exp-07.py

from tkinter import *

form = Tk()

def bt_click():

	if(str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
		num1 = int(ed1.get())
		num2 = int(ed2.get())

		lb["text"] = num1 + num2
	else:
		lb["text"] = "Inválido!"


lb1 = Label(form, text="Entre com o valor de A =")
lb1.place(x=10, y=20)

ed1 = Entry(form, bg="white", width=5)
ed1.place(x=180, y=20)

lb2 = Label(form, text="Entre com o valor de B =")
lb2.place(x=10, y=50)

ed2 = Entry(form, bg="white", width=5)
ed2.place(x=180, y=50)

bt = Button(form, text="SOMA", width=5, command=bt_click)
bt.place(x=240, y=50)

lb3 = Label(form, text="O valor de A+B =")
lb3.place(x=10, y=80)

lb = Label(form)
lb.place(x=180, y=80)

form.geometry("350x110+200+200")
form.title("Soma entre 2 números")

form.mainloop()
