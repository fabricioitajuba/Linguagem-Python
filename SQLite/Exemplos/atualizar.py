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
def AtualizaDado(id, nome, nota):

	sql = "UPDATE notas SET nome='"+nome+"', nota='"+nota+"' WHERE id='"+id+"'"
	try:
		conexao = ConexaoBanco()
		c = conexao.cursor()
		c.execute(sql)
		conexao.commit()
		print("Dado atualizado")
	except Error as ex:
		print(ex)

AtualizaDado("10", "Andreia", "20")