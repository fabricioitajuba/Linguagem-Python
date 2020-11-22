# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#22/11/2020
#TreeView - Inserção simples
#para executar: $ python main01.py

from tkinter import *
from tkinter import ttk

form = Tk()
form.title("TreeView - Inserção simples")
form.geometry("600x300")

tv = ttk.Treeview(form, columns=('id', 'nome', 'fone'), show='headings')

tv.column('id', minwidth=0, width=50)
tv.column('nome', minwidth=0, width=250)
tv.column('fone', minwidth=0, width=100)

tv.heading('id', text='ID')
tv.heading('nome', text='NOME')
tv.heading('fone', text='TELEFONE')

tv.pack()

tv.insert("", "end", values=('10', 'bruno', '1234'))

form.mainloop()