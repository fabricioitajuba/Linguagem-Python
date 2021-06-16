# -*- coding: utf-8 -*-
#Fabricio de Lima Ribeiro
#16/06/2021
#Cálculo do indutor EE
#para executar: $ python indutor-EE.py

import math

## Constantes
#Fator de enrolamento
k=0.7
#Máxima densidade de fluxo magnético [T]
Bmax=0.3
#Máxima densidade de corrente elétrica [A/cm²]
Jmax=450
#Variação máxima de corrente [%]
dI = 20
#uo [ar]
uo=4*math.pi*math.pow(10,-7)

#Entrada
print("Entre com a indutância [uH]:")
L = float(input())
L /= math.pow(10,6)

print("Entre com a corrente média [A]:")
Imed = float(input())

print("Entre com a variação máxima de corrente [%]:")
dI = int(input())

#Corrente de pico
Ipk = Imed*((100+dI)/100)

#Produto das áreas
AeAw=round(((L*math.pow(Ipk,2))/(k*Bmax*Jmax))*math.pow(10,4),2)

#Escolha do núcleo
if AeAw < 0.08:
  Núcleo = "E-20"
  Ae=0.312
elif AeAw >= 0.08 and AeAw < 0.48:
  Núcleo = "E-30/7"
  Ae=0.6
elif AeAw >= 0.48 and AeAw < 1.02:
  Núcleo = "E-30/14"
  Ae=1.2
elif AeAw >= 1.02 and AeAw < 2.84:
  Núcleo = "E-42/15"
  Ae=1.81
elif AeAw >= 2.84 and AeAw < 3.77:
  Núcleo = "E-42/20"
  Ae=2.4
elif AeAw >= 3.77 and AeAw < 8.85:
  Núcleo = "E-55"
  Ae=3.54      
else:
  Núcleo = "Não presente no banco de dados"
  Ae=1

#Número de espiras
N = math.ceil(((L*Ipk)/(Bmax*Ae))*math.pow(10,4))

#Entreferro
lg = round(((math.pow(N,2)*uo*Ae)/L)*math.pow(10,-1),3)

print('Núcleo utilizado: ' + Núcleo)
print('Produto das áreas AeAw: ' + str(round(AeAw,3)) + " [cm4]")
print('Número de espiras: ' + str(N) + " [espiras]")
print('Entreferro: ' + str(lg) + " [mm]")
