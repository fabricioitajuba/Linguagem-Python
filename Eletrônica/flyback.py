# -*- coding: utf-8 -*-
#Fabricio de Lima Ribeiro
#09/06/2021
#Cálculo do conversor flyback
#para executar: $ python flyback.py

import math

#Entre com a tensão de entrada [V]:
Vi=125
#Entre com a variação máxima de entrada [%]:
Vip=20

#Entre com a tensão de saída [V]:
Vo=18
#Entre com a corrente máxima de saída [A]:
Io=1

#Entre com a tensão de saída auxiliar [V]:
Voaux=15
#Entre com a corrente máxima de saída auxiliar [A]:
Ioaux=0.05

#Entre com a frequencia de operação [kHz]:
Fs=40
#Entre com a máxima razão cíclica:
Dmax=0.45
#Entre com o rendimento esperado [%]:
n=70

#Parâmetros do transistor IRF840:
RDSon=1.1
tr=120*math.pow(10,-9)
tf=140*math.pow(10,-9)

#Características términcas:
Tamb=50    #[°C]
Tjmax=100  #[°C]
Rthcd=0.25 #[°C/W]
Rthjc=1    #[°C/W]

## Constantes
#Fator de utilização do primário
kp=0.5
#Fator de utilização da área do enrolamento
kw=0.4
#Densidade de corrente nos condutores
J=300
#Densidade máxima de corrente nos condutores
Jmax=350
#Queda de tensão nos diodos
Vd=1
#Densidade de fluxo magnético
dB=0.18
#Máxima variação da densidade de fluxo magnético
dBmax=0.2
#uo
uo=4*math.pi*math.pow(10,-7)

#Ajustes
Fs=Fs*math.pow(10,3)
n=n/math.pow(10,2)

# Entrada
#print("Entre com a tensão de entrada [V]:")
#Vi = float(input())
#print("Entre com a variação máxima de entrada [%]:")
#Vip = int(input())

# Saída
#print("Entre com a tensão de saída [V]:")
#Vo = float(input())
#print("Entre com a corrente máxima de saída [A]:")
#Io = float(input())

# Saída auxiliar
#print("Entre com a tensão de saída auxiliar [V]:")
#Voaux = float(input())
#print("Entre com a corrente máxima de saída auxiliar [A]:")
#Ioaux = float(input())

# Característica do conversor
#print("Entre com a frequencia de operação [kHz]")
#Fs = int(input())*1000
#print("Entre com a máxima razão cíclica")
#Dmax = float(input())
#print("Entre com o rendimento esperado [%]")
#n = int(input())/100

#Tensão de entrada máxima
Vimax=Vi*((100+Vip)/100)
#Tensão de entrada mínima
Vimin=Vi*((100-Vip)/100)
#Potência total de saída
Po=(Vo*Io)+(Voaux*Ioaux)
#Potência total de entrada
Pin=Po/n

##Cálculo do transformador
#Produto das áreas
AeAw=round((1.1*Po*10000)/(kp*kw*J*Fs*dB),2)
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

#Entreferro total
d=(2*uo*Po*math.pow(10,4))/(math.pow(dB,2)*Ae*math.pow(10,-2)*n*Fs)
#Entreferro
lg=d/2
#Corrente do primário
Ip=(2*Po)/(n*Vimin*Dmax)
#Número de espiras do primário
Np=(dB*d*math.pow(10,4))/(0.4*math.pi*Ip)
#Número de espiras do secundário
Ns=Np*(((Vo+Vd)*(1-Dmax))/(Vimin*Dmax))
#Número de espiras do secundário auxiliar
Naux=Np*(((Voaux+Vd)*(1-Dmax))/(Vimin*Dmax))
#Ciclo de trabalho do conversor
Dnom=(Np*(Vo+Vd))/(Np*(Vo+Vd)+Ns*Vi)
Dmin=(Np*(Vo+Vd))/(Np*(Vo+Vd)+Ns*Vimax)
#Dmax=(Np*(Vo+Vd))/(Np*(Vo+Vd)+Ns*Vimin)
#Indutância do primário
Lp=(Vimin*Dmax)/(Ip*Fs)

#Capacitores de saida
#Ondulação de tensão na saída
dVo=Vo*0.05
#Capacitor de saida
Co=(Io*Dmax)/(Fs*dVo)
#Ondulação de tensão na saída auxiliar
dVoaux=Voaux*0.05
#Capacitor de saida auxiliar
Coaux=(Ioaux*Dmax)/(Fs*dVoaux)

#Correntes de pico nos enrolamentos secundários
Iso=(2*Io)/(1-Dmax)
Isaux=(2*Ioaux)/(1-Dmax)

#RSE dos capacitores
RSEo=dVo/Iso
RSEaux=dVoaux/Isaux

#Tensão de pico nos diodos
Vdpks=Vo+Vimax*(Ns/Np)
Vdpkaux=Voaux+Vimax*(Ns/Np)

#Corrente eficaz nos enrolamentos
Ipef=Ip*math.sqrt(Dmax/3)
Ioef=Io*math.sqrt(Dmax/3)
Iauxef=Isaux*math.sqrt(Dmax/3)

#Area dos condutores
Scup=Ipef/J
Scus=Ioef/J
Scuaux=Iauxef/J

#Dimensionamento do transistor
VSmáx=Vimax*(1/(1-Dmax))
ISmed=(Ns/Np)*(Io+Ioaux)
ISef=((Vimax*Ip)/(Vimin*Dmax))*math.sqrt((math.pow(Dmax,3))/3)
#Perda por condução
Pcond=RDSon*math.pow(ISef,2)
#Perda por comutação
Pcom=Fs/2*(tr+tf)*Ip*VSmáx
#Perdas totais no transistor
Ptotal=Pcond+Pcom

#Características términcas
Rthda=(Tjmax-Tamb-Ptotal*Rthjc)/Ptotal

Cs=(Ip*tf)/Vimin
tonmin=Dmin/Fs
Rs=tonmin/(3*Cs)
Ides=Vimin/Rs
Pr=(Cs*math.pow(Vimin,2)*Fs)/2

#Ajustes
Fs /= 1000
n *= 100
Co *= math.pow(10,6)
Lp *= math.pow(10,6)
Coaux *= math.pow(10,6)
Cs *= math.pow(10,9)

print('\n### Entrada:')
print('Tensão mínima de entrada: ' + str(Vimin) + " [V]")
print('Tensão nominal de entrada: ' + str(Vi) + " [V]")
print('Tensão máxima de entrada: ' + str(Vimax) + " [V]")

print('\n### Saída:')
print('Tensão de saída: ' + str(Vo) + " [V]")
print('Corrente de máxima de saída: ' + str(Io) + " [A]")

print('\n### Saída auxiliar:')
print('Tensão de saída auxiliar: ' + str(Voaux) + " [V]")
print('Corrente de máxima de saída auxiliar: ' + str(Ioaux) + " [A]")

print('\n### Características do conversor:')

print('Frequência de operação: ' + str(Fs) + " [kHz]")
print('Máxima razão cíclica: ' + str(Dmax))

print('Rendimento esperado: ' + str(n) + " [%]")
print('\nPotência total de saída: ' + str(Po) + " [W]")
print('\nPotência total de entrada: ' + str(round(Pin,2)) + " [W]")

print('\n### Transformador:')
print('Núcleo utilizado: ' + Núcleo)
print('Produto das áreas AeAw: ' + str(round(AeAw,3)) + " [cm4]")
#print('Entreferro total: ' + str(round(d*10,3)) + " [mm]")
print('Entreferro: ' + str(round(lg*10,3)) + " [mm]")
print('\nCorrente de pico do primário: ' + str(round(Ip,3)) + " [A]")
print('Número de espiras do primário: ' + str(round(Np,0)) + " [Espiras]")
print('Número de espiras do secundário: ' + str(round(Ns,0)) + " [Espiras]")
print('Número de espiras do secundário auxiliar: ' + str(round(Naux,0)) + " [Espiras]")
print('Indutância do primário: ' + str(round(Lp,0)) + " [uH]")

print('\nCorrente de pico no enrolamento secundário: ' + str(round(Iso,3)) + " [A]")
print('Corrente de pico no enrolamento secundário auxiliar: ' + str(round(Ioaux,3)) + " [A]")

print('\nTensão máxima reversa no diodo de saída: ' + str(round(Vdpks,2)) + " [V]")
print('Tensão máxima reversa no diodo de saida auxiliar: ' + str(round(Vdpkaux,2)) + " [V]")

print('\nCorrente eficaz no primário: ' + str(round(Ipef,3)) + " [A]")
print('Corrente eficaz no secundário: ' + str(round(Ioef,3)) + " [A]")
print('Corrente eficaz no secundário auxiliar: ' + str(round(Iauxef,3)) + " [A]")

print('\nÁrea do condutor primário: ' + str(Scup) + " [cm²]")
print('Área do condutor secundário: ' + str(Scus) + " [cm²]")
print('Área do condutor auxiliar: ' + str(Scuaux) + " [cm²]")

print('\nCapacitor de saída: ' + str(round(Co,2)) + " [uF]")
print('Capacitor de saída auxiliar: ' + str(round(Coaux,2)) + " [uF]")
print('\nResistência série equivalente do capacitor de saida: ' + str(round(RSEo,3)) + " [ohm]")
print('Resistência série equivalente do capacitor de saida auxiliar: ' + str(round(RSEaux,3)) + " [ohm]")

print('\nTensão máxima sobre o transistor: ' + str(round(VSmáx,2)) + " [V]")
print('Corrente média no transistor: ' + str(round(ISmed,3)) + " [A]")
print('Corrente eficaz no transistor: ' + str(round(ISef,3)) + " [A]")
print('Perda por condução: ' + str(round(Pcond,3)) + " [W]")
print('Perda por comutação: ' + str(round(Pcom,3)) + " [W]")
print('Perda total: ' + str(round(Ptotal,3)) + " [W]")

print('\nResistividade términa entre o dissipador e o ambiente: ' + str(round(Rthda,2)) + " [°C/W]")

print('\nCiclo de trabalho minimo: ' + str(round(Dmin,3)) + ' para Vin= ' + str(Vimax))
print('Ciclo de trabalho nominal: ' + str(round(Dnom,3)) + ' para Vin= ' + str(Vi))
print('Ciclo de trabalho máximo: ' + str(round(Dmax,3)) + ' para Vin= ' + str(Vimin))

print('\n### Snubber RCD')
print('Cs= ' + str(round(Cs,3)) + ' [nF]')
print('Rs= ' + str(round(Rs,3)) + ' [ohms]')
print('Idescarga= ' + str(round(Ides,3)) + ' [A]')
print('Ip= ' + str(round(Ip,3)) + ' [A]')
print('Potência dissipada no resistor= ' + str(round(Pr,3)) + ' [W]')
