# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#07/11/2020
#Formulário no centro da tela
#para executar: $ python Exp-06.py

from Tkinter import * 				#importação da classe

form = Tk() 						#método construdor

form.title("Esse é o título") 		#Insere um título

#dimensões do meu formulário
largura = 500
altura = 200

#resolução da tela do meu computador
largura_screen  = form.winfo_screenwidth() #recebe o valor da largura do meu monitor
altura_screen  = form.winfo_screenheight() #recebe o valor da altura do meu monitor

#posição da janela
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

#definir a geometry
form.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

print(largura_screen, altura_screen)

form.mainloop() 					#método principal

