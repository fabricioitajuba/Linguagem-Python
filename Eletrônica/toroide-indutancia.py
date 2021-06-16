# -*- coding: utf-8 -*-
#Fabricio de Lima Ribeiro
#18/12/2020
#Cálculo do toróide

import math


print("Entre com a permeabilidade relativa do material ur:")
ur = int(input())

print("Entre com o número de espiras do indutor:")
N = int(input())

print("Entre com a área esfetiva do núcleo [cm²]:")
Ae = float(input())

print("Entre com o comprimento esfetivo do núcleo [cm]:")
le = float(input())

pi = 3.1415
u = ur
L = (0.4 * pi * ur * N**2 * Ae *10**-8)/le

print(' ')
print('Indutância = ' + str(L) + " [H]")
L *= 10**6
print('Indutância = ' + str(round(L,2)) + " [uH]")
print(' ')
