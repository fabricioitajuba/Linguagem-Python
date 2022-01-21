# -*- coding: utf-8 -*-
#Fabricio de Lima Ribeiro
#16/06/2021
#Cálculo do indutor EE
#para executar: $ python indutor-EE.py

import os
import math

#Limpa a tela do console
os.system('cls')

#Teste
Teste = 0

## Constantes
#Fator de enrolamento
k=0.7
#Máxima densidade de fluxo magnético [T]
Bmax=0.30
#Máxima densidade de corrente elétrica [A/cm²]
Jmax=450
#uo [ar]
uo=4*math.pi*math.pow(10,-7) #[Wb/A/m]

#Entrada
print("Entre com a indutância [uH]:")
L = float(input())
L /= math.pow(10,6)

print("Entre com a corrente média [A]:")
Imed = float(input())

print("Entre com a frequência de operação [kHz]:")
Fs = float(input())
Fs *= math.pow(10,3)

print("Entre com a variação máxima de corrente [%]:")
dI = int(input())

#Corrente de pico
Ipk = Imed*((100+(dI/2))/100)

#Produto das áreas
AeAw=round(((L*math.pow(Ipk,2))/(k*Bmax*Jmax))*math.pow(10,4),2)

#Escolha do núcleo
if AeAw < 0.08:
  Núcleo = "E-20"
  Ae=0.312
  Aw=0.26
  Ve=1.34
  It=3.8
elif AeAw >= 0.08 and AeAw < 0.48:
  Núcleo = "E-30/7"
  Ae=0.6
  Aw=0.8
  Ve=4
  It=5.6
elif AeAw >= 0.48 and AeAw < 1.02:
  Núcleo = "E-30/14"
  Ae=1.2
  Aw=0.85
  Ve=8
  It=6.7
elif AeAw >= 1.02 and AeAw < 2.84:
  Núcleo = "E-42/15"
  Ae=1.81
  Aw=1.57
  Ve=17.1
  It=8.7
elif AeAw >= 2.84 and AeAw < 3.77:
  Núcleo = "E-42/20"
  Ae=2.4
  Aw=1.57
  Ve=23.3
  It=10.5
elif AeAw >= 3.77 and AeAw < 8.85:
  Núcleo = "E-55"
  Ae=3.54 
  Aw=2.5
  Ve=42.5     
  It=11.6
else:
  Núcleo = "Não presente no banco de dados"
  Ae=1

#Número de espiras
N = math.ceil(((L*Ipk)/(Bmax*Ae))*math.pow(10,4))
#Entreferro total
delta = round(((math.pow(N,2)*uo*Ae)/L)*math.pow(10,-1),3)
#Entreferro
lg = delta/2

###Teste
if Teste == 1:
  Ipk=10.5
  Imed=10
  Bmax=0.35
  Fs=20000
  Ve=8
  N=24
  It=6.7
  AeAw=1.02
  Aw=0.85
###

#Perdas no núcleo
KH=4*math.pow(10,-5)
KE=4*math.pow(10,-10)

Iond=(Ipk-Imed)*2
deltaB=Bmax*(Iond/Imed)

Pnucleo=round((math.pow(deltaB, 2.4)*(KH*Fs+KE*math.pow(Fs, 2))*Ve),6)

#Profundidade e penetração
skin=7.5/math.sqrt(Fs)
Dfiomax=round(2*skin,3)

print('\nEntre com a área de cobre de um condutor que possua um diâmetro menor que: ' + str(Dfiomax) + " [cm]")
Acu = float(input())
print('Entre com a área de isolamento do condutor escolhido: [cm²]')
Aiso = float(input())
print('Entre com a resistência do condutor a 20ºC: ')
p = float(input())

###Teste
if Teste == 1:
  Imed=6
  Acu=0.003255
  Aiso=0.004013
  p=0.000530
###

S=round((Imed/Jmax),3)

if S > Acu:
  Nfios=round(S/Acu)
else:
  Nfios=Acu

### Teste
if Teste == 1:
  Nfios=5
###

#Resistência do fio
Rfio=round(N*(p/Nfios)*It, 3)

#Perda no cobre
Pcu=round(Rfio*math.pow(Imed,2), 3)

#Perda total
Pt=round(Pnucleo+Pcu,3)

#Elevação de temperatura
Rt=round(23*math.pow(AeAw, -0.37), 3)
dT=round(Rt*Pt, 3)

#Fator de ocupação
Awnecess=round((N*Nfios*Aiso)/0.7, 3)
Kocup=round(Awnecess/Aw, 3)

#Resultados
print('\nNúcleo utilizado: ' + Núcleo)

### Teste
if Teste == 1:
  print('Produto das áreas AeAw: ' + str(round(AeAw,3)) + " [cm4]")

print('Número de espiras: ' + str(N) + " [espiras]")
print('Entreferro total: ' + str(delta) + " [mm]")
print('Entreferro: ' + str(lg) + " [mm] (cada lado)")

### Teste
if Teste == 1:
  print('\nPerda no núcleo: ' + str(Pnucleo) + " [W]")
  print('Diâmetro do fio máximo: ' + str(Dfiomax) + " [cm]")
  print('Área do condutor: ' + str(S) + " [cm²]")

print('Número de fios em paralelo: ' + str(Nfios) + " [fios]")

### Teste
if Teste == 1:
  print('Resistência do fio: ' + str(Rfio) + " [ohms]")
  print('Perda no cobre: ' + str(Pcu) + " [W]")

print('Perda total: ' + str(Pt) + " [W]")
print('Elevação da temperatura: ' + str(dT) + " [ºC]")

### Teste
if Teste == 1:
  print('Fator de ocupação: ' + str(Kocup))

if Kocup < 1:
  print('É possível fabricar o indutor!')
else:
  print('Não possível fabricar o indutor!')