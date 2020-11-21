# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#21/11/2020
#ProgressBar
#para executar: $ python main01.py

from tkinter import *
from tkinter import ttk

form = Tk()
form.title("ProgressBar 1")
form.geometry("500x300")

#variável que irá alterar o valor da barra
varBarra = DoubleVar()
varBarra.set(20)

pb = ttk.Progressbar(form, variable = varBarra, maximum = 100)
pb.place(x=0, y=0)

form.mainloop()