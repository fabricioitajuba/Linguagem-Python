# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#22/11/2020
#TreeView - Inserção simples
#para executar: $ python main01.py

from tkinter import *
from tkinter import ttk

def btn_inserir():
	msg = "nome"

form = Tk()
form.title("Programa notas")
form.geometry("420x450+100+100")

# Label frame Dados

lbf_dados = LabelFrame(form, text = "Dados", borderwidth = 1, relief = "solid")
lbf_dados.place(x=10, y=10, width=400, height=60)

lb_nome = Label(lbf_dados, text="Nome:")
lb_nome.place(x=10, y=5)

txt_nome = Entry(lbf_dados, bg="white")
txt_nome.place(x=60, y=5)

lb_nota = Label(lbf_dados, text="Nota:")
lb_nota.place(x=260, y=5)

txt_nota = Entry(lbf_dados, bg="white")
txt_nota.place(x=300, y=5, width=60)

# Label frame Controle

lbf_controle = LabelFrame(form, text = "Controle", borderwidth = 1, relief = "solid")
lbf_controle.place(x=10, y=90, width=400, height=60)

btn_inserir = Button(lbf_controle, text="Inserir", command=btn_inserir)
btn_inserir.place(x=10, y=5)

btn_deletar = Button(lbf_controle, text="Deletar", command=btn_inserir)
btn_deletar.place(x=100, y=5)

btn_atualizar = Button(lbf_controle, text="Atualizar", command=btn_inserir)
btn_atualizar.place(x=200, y=5)

btn_atualizar = Button(lbf_controle, text="Consultar", command=btn_inserir)
btn_atualizar.place(x=300, y=5)

# Label frame Tabela

lbf_tabela = LabelFrame(form, text = "Tabela", borderwidth = 1, relief = "solid")
lbf_tabela.place(x=10, y=170, width=400, height=260)

tabela = ttk.Treeview(lbf_tabela, columns=('id', 'nome', 'nota'), show='headings')
tabela.column('id', minwidth=0, width=30)
tabela.column('nome', minwidth=0, width=100)
tabela.column('nota', minwidth=0, width=80)
tabela.heading('id', text='id')
tabela.heading('nome', text='Nome')
tabela.heading('nota', text='Nota')
#tv.pack()
tabela.place(x=10, y=5, width=380, height=220)

form.mainloop()