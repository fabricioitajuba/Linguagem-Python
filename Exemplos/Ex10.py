# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#08/11/2020
#Exemplo de criação de uma clase
#para executar: $ python Ex10.py

#Classe
class Computador:
	def __init__(self, marca, ram, video):
		self.marca = marca
		self.ram = ram
		self.video = video
	#pass

	#métodos
	def Ligar(self):
		print('Estou ligando')

	def Desligar(self):
		print('Estou desligando')

	def ExibirInformaoesDesteComputador(self):
		print(self.marca, self.ram,  self.video)

#método construtor
computador1 = Computador('Asus', '8Bb', 'Nvidia')
computador2 = Computador('Dell', '4Bb', 'GeForce')
computador3 = Computador('Acer', '2Bb', 'ATM')

print(computador1.marca, computador1.ram, computador1.video)
print(computador2.marca, computador2.ram, computador2.video)
print(computador3.marca, computador3.ram, computador3.video)

#utilizando os métodos
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInformaoesDesteComputador()