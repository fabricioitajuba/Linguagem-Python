# -*- coding: utf-8 -*-
#Fabricio de Lima Ribeiro
#17/06/2021
#Cálculo do transformador do conversor flyback
#para executar: $ python flyback.py

import math

#Vetores
Vs = []
Is = []
Ps = []
Ns = []
Ispk = []
Isef = []
Iscu = []
Lms = []

## Constantes
#Fator de utilização do primário
kp=0.5
#Fator de utilização da área do enrolamento
kw=0.4
#Densidade de corrente nos condutores
J=400
#Máxima variação da densidade de fluxo magnético
dB=0.25
#uo
uo=4*math.pi*math.pow(10,-7)

# Entrada
print("Entre com a tensão de entrada [V]:")
Vi = float(input())
print("Entre com a variação máxima de entrada [%]:")
Vip = int(input())

# Saída
print("Entre com o número de saídas:")
nsaidas = int(input())

#Queda nos diodos
print("Entre com a queda de tensão no(s) diodo(s) [V]:")
Vd = float(input())

for x in range(0, nsaidas):
  print("Entre com a tensão da saída-" + str(x+1) + " [V]")
  Vs.append(float(input()))
  print("Entre com a corrente da saída-" + str(x+1) + " [A]")
  Is.append(float(input()))

# Característica do conversor
print("Entre com a frequencia de operação [kHz]")
Fs = int(input())*1000
print("Entre com a razão cíclica máxima (normalmente 0.45)")
Dmax = float(input())
print("Entre com o rendimento esperado [%] (normalmente 70%)")
n = int(input())/100

#Tensão de entrada máxima
Vimax=Vi*((100+Vip)/100)
#Tensão de entrada mínima
Vimin=Vi*((100-Vip)/100)

#Potências nas saídas
for x in range(0, nsaidas):
    Ps.append((Vs[x]+Vd)*Is[x])

#Potência total de saída
Po=0
for x in range(0, nsaidas):
    Po = Po + Ps[x]

#Potência total de entrada
Pin=Po/n

##Cálculo do transformador
#Produto das áreas
#AeAw=round((1.1*Po*10000)/(kp*kw*J*Fs*dB),2)
AeAw=round(((Po/(n*dB*kp*kw*J*Fs))*math.sqrt(4/3*Dmax))*math.pow(10,4),2)

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
#Corrente de pico do primário
Ip=(2*Po)/(n*Vimin*Dmax)
#Corrente eficaz do primário
Ief=Ip*math.sqrt(Dmax/3)
#Área do condutor primário
Scu=Ief/J
#Número de espiras do primário
Np=math.ceil((dB*d*math.pow(10,4))/(0.4*math.pi*Ip))

#Número de espiras dos secundário
for x in range(0, nsaidas):
    Ns.append(math.ceil(Np*(((Vs[x]+Vd)*(1-Dmax))/(Vimin*Dmax))))

#Indutância magnetizante do primário
#Lp=((math.pow(Np,2)*uo*Ae)/d)*math.pow(10,-2)
Lmp=(Np*dB*Ae)/Ip

#Correntes de pico nos enrolamentos secundários
for x in range(0, nsaidas):
    Ispk.append((2*Is[x])/(1-Dmax))
    #Ispk.append(Ip*Np/Ns[x])

#Corrente eficaz nos enrolamentos secundários
for x in range(0, nsaidas):
    Isef.append(Ispk[x]*math.sqrt((1-Dmax)/3))

#Area dos condutores secundários
for x in range(0, nsaidas):
    Iscu.append(Isef[x]/J)

#Indutância magnetizante do secundário:
for x in range(0, nsaidas):
    Lms.append(((Ns[x]*dB*Ae)/Ispk[x])*math.pow(10,2))

#Ciclos de trabalho do conversor
Dnom=(Np*(Vs[0]+Vd))/(Np*(Vs[0]+Vd)+Ns[0]*Vi)
Dmin=(Np*(Vs[0]+Vd))/(Np*(Vs[0]+Vd)+Ns[0]*Vimax)
Dmax=(Np*(Vs[0]+Vd))/(Np*(Vs[0]+Vd)+Ns[0]*Vimin)

#Profundidade de penetração
skin=7.5/math.sqrt(Fs)
dmax=2*skin

#Ajustes
Fs /= 1000
n *= 100
#Lp *= math.pow(10,6)
Lmp *= math.pow(10,2)

print('\n### Transformador:')
print('Núcleo utilizado: ' + Núcleo)
print('Produto das áreas AeAw: ' + str(round(AeAw,3)) + " [cm4]")
print('Entreferro total: ' + str(round(d*10,3)) + " [mm]")
print('Entreferro (dos lados): ' + str(round(lg*10,3)) + " [mm]")
print('Potência total de saída: ' + str(round(Po,3)) + " [W]")
print('Potência total de entrada: ' + str(round(Pin,3)) + " [W]")
print('Profundidade de penetração (efeito skin): ' + str(round(skin,3)) + " [cm]")
print('Diâmetro máximo (efeito skin): ' + str(round(dmax,3)) + " [cm]")

print('\n### Primário:')
print('Corrente de pico do primário: ' + str(round(Ip,3)) + " [A]")
print('Corrente eficaz do primário: ' + str(round(Ief,3)) + " [A]")
print('Área do condutor primário: ' + str(Scu) + " [cm²]")
print('Número de espiras do primário: ' + str(Np) + " [Espiras]")
#print('Indutância do primário: ' + str(round(Lp,3)) + " [uH]")
print('Indutância magnetizante do primário: ' + str(round(Lmp,3)) + " [uH]")

print('\n### Secundário(s):')
for x in range(0, nsaidas):
    print('Corrente de pico no enrolamento secundário-' + str(x+1)  + " = " + str(round(Ispk[x],3)) + " [A]")

for x in range(0, nsaidas):
    print('Corrente eficaz no enrolamento secundário-' + str(x+1)  + " = " + str(round(Isef[x],3)) + " [A]")

for x in range(0, nsaidas):
    print('Área do condutor secundário-' + str(x+1)  + " = " + str(Iscu[x]) + " [cm²]")

for x in range(0, nsaidas):
    print('Número de espiras do secundário-' + str(x+1)  + " = " + str(Ns[x]) + " [Espiras]")

for x in range(0, nsaidas):
    print('Indutância(s) magnetizante(s) do(s) secundário(s)-' + str(x+1)  + " = " + str(round(Lms[x],3)) + " [uH]")

print('\n### Cíclos de trabalho do transformador:')
print('Ciclo de trabalho minimo: ' + str(round(Dmin,2)) + ' para Vin= ' + str(round(Vimax,2)) + ' [V]')
print('Ciclo de trabalho nominal: ' + str(round(Dnom,2)) + ' para Vin= ' + str(round(Vi,2)) + ' [V]')
print('Ciclo de trabalho máximo: ' + str(round(Dmax,2)) + ' para Vin= ' + str(round(Vimin,2)) + ' [V]')

print('\n### Obs:')
print('- Consultar a tabela de fios AWG, achar um condutor com diâmetro do cobre acima da profundidade de penetração;')
print('- O número de condutores em paralelo do secundário é a divisão entre a área de cobre do condutor pela')
print('  área de cobre do condutor achado na tabela. n(condutores)=Ss/Sskin')