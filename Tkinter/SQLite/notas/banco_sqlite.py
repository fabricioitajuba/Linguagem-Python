#SQLite 3 - Funções para trabalhar com o sqlite
#Fabrício de Lima Ribeiro
#06/12/20

import sqlite3
from sqlite3 import Error
from tkinter import messagebox

#Criar a conexao
def ConexaoBanco(banco):

	con = 'Nome'
	try:
		con = sqlite3.connect(banco)
	except Error as ex:
		messagebox.showerror(title="Erro!", message=ex)

	return con

#Executa um comando sql
def ExecutaSQL(conexao, sql):
	
	try:
		c = conexao.cursor()
		c.execute(sql)
		conexao.commit()
	except Error as ex:
		messagebox.showerror(title="Erro!", message=ex)

#Inserir dados
def InserirDados(conexao, nome, nota):

	sql = "INSERT INTO notas (nome, nota) VALUES('"+ nome +"', '"+ nota +"')"
	try:
		c = conexao.cursor()
		c.execute(sql)
		conexao.commit()
	except Error as ex:
		messagebox.showerror(title="Erro!", message=ex)

#Deletar dados
def DeletaDado(conexao, id):

	sql = "DELETE FROM notas WHERE id='"+ id+"'"
	try:
		c = conexao.cursor()
		c.execute(sql)
		conexao.commit()
	except Error as ex:
		messagebox.showerror(title="Erro!", message=ex)

#Atualiza dados
def AtualizaDado(conexao, id, nome, nota):

	sql = "UPDATE notas SET nome='"+nome+"', nota='"+nota+"' WHERE id='"+id+"'"
	try:
		c = conexao.cursor()
		c.execute(sql)
		conexao.commit()
	except Error as ex:
		messagebox.showerror(title="Erro!", message=ex)

#Consultar dados
def ConsultaDado(conexao, nome):

	sql = "SELECT * FROM notas WHERE nome LIKE '"+nome+"%'"
	try:
		c = conexao.cursor()
		c.execute(sql)
		resultado = c.fetchall()
		return resultado
	except Error as ex:
		messagebox.showerror(title="Erro!", message=ex)