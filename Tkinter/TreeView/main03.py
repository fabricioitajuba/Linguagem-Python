# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#22/11/2020
#TreeView - Inserção de campos
#para executar: $ python main03.py

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def inserir():
	if vid.get() == "" or vnome.get() == "" or vfone.get() == "":
		messagebox.showinfo(title = "ERRO", message="Digite todos os dados")
		return

	tv.insert("", "end", values = (vid.get(), vnome.get(), vfone.get()))

	vid.delete(0, END)
	vnome.delete(0, END)
	vfone.delete(0, END)
	vid.focus()

def deletar():
	print()

def obter():
	print()		

form = Tk()
form.title("TreeView - Inserção de campos")
form.geometry("550x350")

lbid = Label(form, text="ID")#, anchor = W)
vid = Entry(form)

lbnome = Label(form, text="Nome")#, anchor = W)
vnome = Entry(form)

lbfone = Label(form, text="Fone")#, anchor = W)
vfone = Entry(form)

tv = ttk.Treeview(form, columns=('id', 'nome', 'fone'), show='headings')

tv.column('id', minwidth=0, width=50)
tv.column('nome', minwidth=0, width=250)
tv.column('fone', minwidth=0, width=100)

tv.heading('id', text='ID')
tv.heading('nome', text='NOME')
tv.heading('fone', text='TELEFONE')

btn_inserir = Button(form, text="Inserir", command=inserir)
btn_deletar = Button(form, text="Deletar", command=deletar)
btn_obter = Button(form, text="obter", command=obter)

lbid.grid(column = 0, row = 0, stick = 'w')
vid.grid(column = 0, row = 1)

lbnome.grid(column = 1, row = 0, stick = 'w')
vnome.grid(column = 1, row = 1)

lbfone.grid(column = 2, row = 0, stick = 'w')
vfone.grid(column = 2, row = 1)

tv.grid(column=0, row=3, columnspan=3, pady=5)

btn_inserir.grid(column = 0, row = 4)
btn_deletar.grid(column = 1, row = 4)
btn_obter.grid(column = 2, row = 4)

#tv.insert("", "end", values=(i, n, f))

form.mainloop()