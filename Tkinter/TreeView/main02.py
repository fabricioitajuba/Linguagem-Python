# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#22/11/2020
#TreeView - Inserção através de uma lista
#para executar: $ python main02.py

from tkinter import *
from tkinter import ttk

form = Tk()
form.title("TreeView - Inserção com lista")
form.geometry("600x300")

tv = ttk.Treeview(form, columns=('id', 'nome', 'fone'), show='headings')

tv.column('id', minwidth=0, width=50)
tv.column('nome', minwidth=0, width=250)
tv.column('fone', minwidth=0, width=100)

tv.heading('id', text='ID')
tv.heading('nome', text='NOME')
tv.heading('fone', text='TELEFONE')

tv.pack()

listaNomes = [['0', 'Fabricio', '1234'], ['1', 'Fabiano', '2345'], ['2', 'Angiene', '3456']]

for(i, n, f) in listaNomes:
	tv.insert("", "end", values=(i, n, f))

form.mainloop()