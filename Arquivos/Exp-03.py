# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#18/11/2020
#Gravação de arquivo texto
#para executar: $ python Exp-03.py

arquivo = open("Exp-03.txt", "w")

for num in range(10):
	arquivo.write(str(num+1)+"\n")

arquivo.close

