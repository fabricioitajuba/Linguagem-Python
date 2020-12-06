# -*- coding: utf-8 -*-
#SQLite 3 - Executa um comando sql
#Fabrício de Lima Ribeiro
#06/12/20

import sqlite3
from sqlite3 import Error

#Criar a conexao
def ConexaoBanco():

	con = 'Nome'
	try:
		con = sqlite3.connect("banco.db")
	except Error as ex:
		print(ex)

	return con

#Executa um comando sql
def ExecutaSQL(sql):
	
	try:
		conexao = ConexaoBanco()
		c = conexao.cursor()
		c.execute(sql)
		conexao.commit()
		print("Comando executado")
	except Error as ex:
		print(ex)

#Cria uma tabela caso ela não exista
sql = "CREATE TABLE IF NOT EXISTS 'notas2' ('id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 'nome' TEXT, 'nota' INTEGER)"
ExecutaSQL(sql)

#Apaga uma tabela
#sql = "DROP TABLE 'notas2'"
#ExecutaSQL(sql)