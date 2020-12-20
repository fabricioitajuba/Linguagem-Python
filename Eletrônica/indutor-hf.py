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

print("Entre com a corrente de pico [A]:")
I = float(input())

print("Entre com a área esfetiva [cm²]:")
Ae = float(input())
Ae /= 10**4

N = math.sqrt(L/Al)

#Cálculo do B da primeira maneira
F = N*I #[AE]
R = 1/Al #[N²/H]
phi = F/R #[Wb]
B = phi/Ae #[Tesla]

#Cálculo do B da segunda maneira
B2 = (L*I)/(Ae*N) #[Tesla]

print(' ')
print('Numero de espiras do indutor = ' + str(round(N,0)) + " espiras")
print('B1= '+str(round(B,2))+' [T]')
print('B2= '+str(round(B2,2))+' [T]')
print(' ')
