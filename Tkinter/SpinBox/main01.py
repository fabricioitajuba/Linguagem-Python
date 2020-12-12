# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#12/11/2020
#SpinBox
#para executar: $ python main01.py

from tkinter import *

app = Tk()
app.title("Scale")
app.geometry("500x300")

sb_valores = Spinbox(app, from_=0, to=100)
sb_valores.pack()

app.mainloop()