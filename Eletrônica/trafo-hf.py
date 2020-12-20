# -*- coding: utf-8 -*-
#Fabricio de Lima Ribeiro
#13/12/2020
#Cálculo do transformador casador de impedância
#para executar: $ python3 trafo-hf.py

import math


print("Entre com o nucleo escolhido:")
nucleo = input()

print("Entre com a tensão do primário [Vp]:")
Ep = float(input())

print("Entre com a Impedancia do primário [ohms]:")
Zp = float(input())

print("Entre com a Impedancia do secundário [ohms]:")
Zs = float(input())

print("Entre com a frequencia mínima de operação [kHz]")
F = int(input())*1000

print("Entre com o Al do nucleo escolhido [nH/n^2]")
Al = float(input())
Al = Al*math.pow(10,-9)

print("Entre com a area efetiva do núcleo [mm^2]:")
Ae = float(input())
Ae = Ae/100

Xp = 4*Zp
Lp = Xp/(2*3.14*F)
Np = int(round(math.sqrt(Lp/Al), 0))
Ns = int(round(Np * math.sqrt(Zs/Zp), 0))
B = int(round((Ep*math.pow(10, 8))/(4.44*F*Np*Ae), 0))
B2 = B/10**4


print(' ')
print('Nucleo escolhido: ' + nucleo)
print(' ')
print('### Lado primario ###')
print('Impedancia do primário: ' + str(Zp) + " ohms")
print('Numero de espiras do primário = ' + str(Np) + " espiras")
print(' ')
print('### Lado secundario ###')
print('Impedancia do secundário: ' + str(Zs) + " ohms")
print('Numero de espiras do secundário = ' + str(Ns) + " espiras")
print(' ')
print('### Diversos ###')
print('B= '+str(B)+' [Gauss] ou '+str(B2*1000)+' [mT]')