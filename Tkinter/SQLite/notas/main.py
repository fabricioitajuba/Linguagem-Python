# -*- coding: utf-8 -*-
#Exemplo de utilização do banco SQLite 3
#Fabrício de Lima Ribeiro
#06/12/20

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import banco_sqlite as bd

# Funções

#Função para inserir dado
def btn_inserir():

	res = messagebox.askyesno("Exemplo com SQLite", "Deseja realmente inserir?")

	if res:
		bd.InserirDados(con, txt_nome.get(), txt_nota.get())
		txt_nome.delete(0, 'end')
		txt_nota.delete(0, 'end')
		atualiza_tabela()

#Função para consultar dado(s)
def btn_consultar():
	#Deleta todo co conteúdo da tabela
	tabela.delete(*tabela.get_children())
	#Faz a consulta de todos ou um elemento do banco
	res = bd.ConsultaDado(con, txt_nome.get())
	#Envia-os para a tabela
	for i in res:
		tabela.insert("", "end", values = i)

#Função para atualizar tabela
def atualiza_tabela():
	#Deleta todo co conteúdo da tabela
	tabela.delete(*tabela.get_children())
	#Faz a consulta de todos os elemento do banco
	res = bd.ConsultaDado(con, "")
	#Envia-os para a tabela
	for i in res:
		tabela.insert("", "end", values = i)

# Rotinas iniciais

#Realiza a conexao com o banco de dados. Caso não exista o mesmo será criado
con = bd.ConexaoBanco("banco.db")

#Cria uma tabela caso ela não exista
sql = "CREATE TABLE IF NOT EXISTS 'notas' ('id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 'nome' TEXT, 'nota' INTEGER)"
bd.ExecutaSQL(con, sql)

#Criação do formulário
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

btn_atualizar = Button(lbf_controle, text="Consultar", command=btn_consultar)
btn_atualizar.place(x=300, y=5)

# Label frame Tabela
lbf_tabela = LabelFrame(form, text = "Tabela", borderwidth = 1, relief = "solid")
lbf_tabela.place(x=10, y=170, width=400, height=260)
#Criação da tabela
tabela = ttk.Treeview(lbf_tabela, columns=('id', 'nome', 'nota'), show='headings')
tabela.column('id', minwidth=0, width=30)
tabela.column('nome', minwidth=0, width=100)
tabela.column('nota', minwidth=0, width=80)
tabela.heading('id', text='id')
tabela.heading('nome', text='Nome')
tabela.heading('nota', text='Nota')
tabela.place(x=10, y=5, width=380, height=220)
#Preenche a tabela com os dados do banco
atualiza_tabela()

form.mainloop()