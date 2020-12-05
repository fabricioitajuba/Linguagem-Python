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
def ConsultaDado(nome):

	sql = "SELECT * FROM notas WHERE nome LIKE '"+nome+"%'"
	try:
		conexao = ConexaoBanco()
		c = conexao.cursor()
		c.execute(sql)
		resultado = c.fetchall()
		return resultado
	except Error as ex:
		print(ex)

resposta=ConsultaDado("")

for i in resposta:
	print(i)