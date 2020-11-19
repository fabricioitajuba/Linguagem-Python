# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#18/11/2020
#Leitura de arquivo texto
#para executar: $ python Exp-04.py

arquivo = open("Exp-03.txt")

for linha in arquivo:
	print(linha.rstrip())

arquivo.close

