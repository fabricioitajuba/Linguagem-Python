#SQLite 3 - Funções para trabalhar com o sqlite
#Fabrício de Lima Ribeiro
#13/12/20

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

#Executa um comando sql sem retorno
def Envia_SQL(conexao, sql):
	
	try:
		c = conexao.cursor()
		c.execute(sql)
		conexao.commit()
	except Error as ex:
		messagebox.showerror(title="Erro!", message=ex)

#Executa um comando sql com retorno
def Recebe_SQL(conexao, sql):

	try:
		c = conexao.cursor()
		c.execute(sql)
		resultado = c.fetchall()
		return resultado
	except Error as ex:
		messagebox.showerror(title="Erro!", message=ex)