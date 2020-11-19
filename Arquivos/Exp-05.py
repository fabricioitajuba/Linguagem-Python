# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#18/11/2020
#Gravação de arquivo binário
#para executar: $ python Exp-05.py

import pickle

arquivo = open("Exp-05.dat", "wb")

pickle.dump(76, arquivo)

arquivo.close

