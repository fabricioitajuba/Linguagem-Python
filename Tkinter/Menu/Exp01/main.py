# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#28/11/2020
#Exemplo de criação de menu
#para executar: $ python main.py

#import os #para uma pasta específica
from tkinter import *

#pastaTelas = os.path.dirname(__file__)#para uma pasta específica

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def novaJanela():
	#exec(open(pastaTelas + "tela1.py").read())#para uma pasta específica
	#exec(open("tela1.py").read()) # sem enviar parâmetros
	exec(open("tela1.py").read(), {'x':10}) # enviar parâmetros

form = Tk()

#Criação do menu
menubar = Menu(form)
#Menu File
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=novaJanela)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=form.quit)
menubar.add_cascade(label="File", menu=filemenu)

form.config(menu=menubar)

form.geometry("750x450+100+100")
form.resizable(False, False)
form.title("Exemplo de criação de menus")

form.mainloop()