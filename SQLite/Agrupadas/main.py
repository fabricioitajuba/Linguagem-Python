# -*- coding: utf-8 -*-
#Exemplo de utilização do banco SQLite 3
#Fabrício de Lima Ribeiro
#13/12/20

import banco_sqlite as bd

def cria_tabela(con):
	sql = "CREATE TABLE IF NOT EXISTS 'notas' ('id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 'nome' TEXT, 'nota' INTEGER)"
	bd.Envia_SQL(con, sql)

def insere_dados(con, nome, nota):
	sql = "INSERT INTO notas (nome, nota) VALUES('"+ nome +"', '"+ nota +"')"
	bd.Envia_SQL(con, sql)

def deleta_dados(con, id):
	sql = "DELETE FROM notas WHERE id='"+ id+"'"
	bd.Envia_SQL(con, sql)

def atualiza_dados(con, id, nome, nota):
	sql = "UPDATE notas SET nome='"+nome+"', nota='"+nota+"' WHERE id='"+id+"'"
	bd.Envia_SQL(con, sql)

def consulta_dado(con, nome):
	sql = "SELECT * FROM notas WHERE nome LIKE '"+nome+"%'"
	res = bd.Recebe_SQL(con, sql)
	return res


# Programa principal

#Realiza a conexao com o banco de dados. Caso não exista o mesmo será criado
con = bd.ConexaoBanco("banco.db")

#Cria uma tabela caso ela não exista
cria_tabela(con)

#Insere dados
insere_dados(con, "Fabrício", "100")

#Insere dados
insere_dados(con, "Angiene", "90")

#Insere dados
insere_dados(con, "Fabiano", "10")

#Insere dados
insere_dados(con, "Andréia", "70")

#Insere dados
insere_dados(con, "Expedito", "15")

#Deleta dado
deleta_dados(con, "5")

#Atualiza dado
atualiza_dados(con, "3", "Fabiano", "50")

#Consulta dado
res = consulta_dado(con, "Fabiano")
print(res)

#Consulta dados
res = consulta_dado(con, "")
print(res)