# -*- coding: utf-8 -*-
#Gravação de arquivo csv

arquivo = open("dados.csv", "w")

#arquivo.write("T_ms;Xa;Xb;Xc\n")

t = 0
Xa = 0
Xb = 0
Xc = 0

for i in range(0, 100):
	arquivo.write(format(t, '.1f')+";"+str(Xa)+";"+str(Xb)+";"+str(Xc)+"\n")
	t += 0.1

Xa = 1

for i in range(0, 10):
	arquivo.write(format(t, '.1f')+";"+str(Xa)+";"+str(Xb)+";"+str(Xc)+"\n")	
	t += 0.1

Xa = 1
Xb = 1

for i in range(0, 10):
	arquivo.write(format(t, '.1f')+";"+str(Xa)+";"+str(Xb)+";"+str(Xc)+"\n")	
	t += 0.1

Xa = 1
Xb = 1
Xc = 1

for i in range(0, 80):
	arquivo.write(format(t, '.1f')+";"+str(Xa)+";"+str(Xb)+";"+str(Xc)+"\n")	
	t += 0.1

arquivo.close

