# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#18/11/2020
#Gravação de arquivo binário
#para executar: $ python Exp-08.py

import pickle

arquivo = open("Exp-07.dat", "rb")

for i in range(10):
	n = pickle.load(arquivo)
	print(n)

arquivo.close

