# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#06/12/2020
#Exemplos de Messagebox
#para executar: $ python main01.py

from tkinter import *
from tkinter import messagebox

form = Tk()
form.title("Exemplos de Messagebox")
form.geometry("500x300")

#info
messagebox.showinfo(title="Info", message="Exemplo1")

#warning
messagebox.showwarning(title="wearning", message="Exemplo2")

#error
messagebox.showerror(title="error", message="Exemplo3")

#Sim, não (True or False)
res = messagebox.askyesno("Exemplo4", "Confirma?")
print(res)

#Ok, Cancelar (True or False)
res = messagebox.askokcancel("Exemplo5", "Confirma?")
print(res)

#Repetir, Cancelar (True or False)
res = messagebox.askretrycancel("Exemplo6", "Confirma?")
print(res)

#Sim, Não, Cancelar (True, False, Nome)
res = messagebox.askyesnocancel("Exemplo7", "Confirma?")
print(res)

mainloop()