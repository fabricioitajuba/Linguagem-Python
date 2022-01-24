# -*- coding: utf-8 -*-
#Fabricio de Lima Ribeiro
#16/06/2021
#Cálculo do indutor EE
#para executar: $ python indutor-EE.py

import os
import math

#Limpa a tela do console
os.system('cls')

#Entrada
print("Entre com a indutância [uH]:")
L=float(input())
L /= math.pow(10,6)

print("Entre com o AL [nH/N²]:")
AL=float(input())
AL /= math.pow(10,9)

print("Entre com a densidade máxima do fluxo magnético [T]:")
Bmax=float(input())

print("Entre com a corrente de pico [A]:")
Ipk=float(input())

print("Entre com a área efetiva do núcleo [cm²]:")
Ae=float(input())
Ae /= math.pow(10,4)

#Número de espiras
N=round(math.sqrt(L/AL), 0)

F=N*Ipk
R=1/AL
phi=F/R
B=round(phi/Ae, 3)

#Resultados
print('\n --- Resultados: ')
print('Número de espiras: ' + str(N) + " [espiras]")
print('Força magnetomotriz F= ' + str(F) + " [AE]")
print('Relutância do núcleo R= ' + str(R) + " [E²/H]")
print('Fluxo magnético do núcleo phi= ' + str(phi) + " [Wb]")
print('Campo induzido no núcleo B= ' + str(B) + " [T]")

if B <= Bmax:
    print('O indutor não irá saturar! B <= Bmax ')
else:
        print('O indutor irá saturar! B > Bmax ')

print('---')