# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#18/11/2020
#Gravação de arquivo binário
#para executar: $ python Exp-06.py

import pickle

arquivo = open("Exp-05.dat", "rb")

n = pickle.load(arquivo)
print(n)

arquivo.close

