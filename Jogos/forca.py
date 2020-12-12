# -*- coding: utf-8 -*-
#Fabricio de Lima Ribeiro
#12/11/2020
#Jogo da forca

from tkinter import *

def jogar():

	global palavra
	palavra = txt_palavra.get()
	txt_palavra.delete(0, 'end')
	global tamanho
	tamanho = len(palavra)
	
	global label
	label = {}

	for i in range(0, tamanho):
	    lb = Label(app, text=" ___ ")
	    lb.place(x=i*30, y=120)
	    label[i] = lb


def advinhar():
	letra = txt_letra.get()
	txt_letra.delete(0, 'end')

	for i in range(0, tamanho):
		if letra == palavra[i]:
			label[i]['text'] = palavra[i]
	

app = Tk()
app.title("Jogo da forca")
app.geometry("500x300")

#Entra com a palavra
lb_1 = Label(app, text="Entre com a palavra: ")
lb_1.place(x=5, y=6)

txt_palavra = Entry(app, bg="white", width=15)
txt_palavra.place(x=150, y=7)

btn_jogar = Button(app, text="Jogar", command=jogar)
btn_jogar.place(x=280, y=4)

#Entra com a letra
lb_3 = Label(app, text="Entre com uma letra: ")
lb_3.place(x=5, y=56)

txt_letra = Entry(app, bg="white", width=15)
txt_letra.place(x=150, y=57)

btn_letra = Button(app, text="advinhar", command=advinhar)
btn_letra.place(x=280, y=54)

app.mainloop()