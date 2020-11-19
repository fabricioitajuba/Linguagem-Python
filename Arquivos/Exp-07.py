# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#18/11/2020
#Gravação de arquivo binário
#para executar: $ python Exp-07.py

import pickle

arquivo = open("Exp-07.dat", "wb")

for i in range(10):
	pickle.dump(i, arquivo)

arquivo.close

