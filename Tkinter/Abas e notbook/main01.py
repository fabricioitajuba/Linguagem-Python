# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#12/11/2020
#Abas e notbook
#para executar: $ python main01.py

from tkinter import *
from tkinter import ttk

app = Tk()
app.title("Abas e notbook")
app.geometry("500x300")

nb = ttk.Notebook(app)
nb.place(x=0, y=0, width=500, height=300)

tb1 = Frame(nb)
tb2 = Frame(nb)

nb.add(tb1, text="Teste1")
nb.add(tb2, text="Teste2")

lb1 = Label(tb1, text="Testes-1")
lb1.pack()

lb2 = Label(tb2, text="Testes-2")
lb2.pack()

app.mainloop()