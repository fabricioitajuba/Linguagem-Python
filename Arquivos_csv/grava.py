# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#18/11/2020
#Gravação de arquivo texto
#para executar: $ python Exp-01.py

arquivo = open("dados.csv", "w")

arquivo.write("T_ms;Xa;Xb;Xc\n")

t = 0
Xa = 0
Xb = 0
Xc = 0

for i in range(0, 200):
	t += 0.1
	arquivo.write(format(t, '.1f')+";"+str(Xa)+";"+str(Xb)+";"+str(Xc)+"\n")

arquivo.close

