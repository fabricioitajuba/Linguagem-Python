# -*- coding: utf-8 -*-
#Fabricio de Lima Ribeiro
#18/12/2020
#Cálculo de indutor com núcleo toroidal
#para executar: $ python3 indutor-hf.py

import math


print("Entre com a indutância desejada em [uH]:")
L = float(input())
L /=10**6

print("Entre com o Al do nucleo escolhido [nH/n²]:")
Al = int(input())
Al /= 10**9

print("Entre com a corrente desejada [A]:")
I = float(input())

print("Entre com a área esfetiva [cm²]:")
Ae = float(input())
Ae /= 10**4

N = int(round(math.sqrt(L/Al), 0))
F = N*I
R = 1/Al
phi = F/R
B = phi/Ae

print(' ')
print('Numero de espiras do indutor = ' + str(N) + " espiras")
print('F='+str(F)+'[AE]')
print('R='+str(R)+'[N²/H]')
print('phi='+str(phi)+'[Wb]')
print('Ae='+str(Ae)+'[m²]')
print('B='+str(round(B,2))+'[Tesla]')
print(' ')
