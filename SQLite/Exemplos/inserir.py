# -*- coding: utf-8 -*-
#SQLite 3 - Conexao com o banco de dados
#Fabrício de Lima Ribeiro
#05/12/20

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

#Inserir dados
def InserirDados(nome, nota):

	sql = "INSERT INTO notas (nome, nota) VALUES('"+ nome +"', '"+ nota +"')"
	try:
		conexao = ConexaoBanco()
		c = conexao.cursor()
		c.execute(sql)
		conexao.commit()
		print("Registro inserido")
	except Error as ex:
		print(ex)

InserirDados("Angiene", "100")