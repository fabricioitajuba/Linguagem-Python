# -*- coding: utf-8 -*-
#Função com vários valores
#Fabrício de Lima Ribeiro
#12/12/20

def funcao():
	a = 1
	b = 2
	return a, b

c, d = funcao()

print(c)
print(d)

e, _ = funcao()

print(e)