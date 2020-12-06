# -*- coding: utf-8 -*-
#Exemplo de utilização do banco SQLite 3
#Fabrício de Lima Ribeiro
#06/12/20

import banco_sqlite as bd

#Realiza a conexao com o banco de dados. Caso não exista o mesmo será criado
con = bd.ConexaoBanco("banco.db")

#Cria uma tabela caso ela não exista
sql = "CREATE TABLE IF NOT EXISTS 'notas' ('id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 'nome' TEXT, 'nota' INTEGER)"
bd.ExecutaSQL(con, sql)

#Insere dados
bd.InserirDados(con, "Fabrício", "100")
#Insere dados
bd.InserirDados(con, "Angiene", "90")
#Insere dados
bd.InserirDados(con, "Fabiano", "10")
#Insere dados
bd.InserirDados(con, "Andréia", "70")
#Insere dados
bd.InserirDados(con, "Expedito", "15")

#Deleta dado
bd.DeletaDado(con, "5")

#Atualiza dado
bd.AtualizaDado(con, "3", "Fabiano", "50")

#Consulta dado
res = bd.ConsultaDado(con, "Fabiano")
print(res)

#Consulta dados
res = bd.ConsultaDado(con, "")
print(res)