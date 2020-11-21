# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#07/11/2020
#Dimensionamento máximo e mínimo
#para executar: $ python main04.py

from Tkinter import * 				#importação da classe

form = Tk() 						#método construdor

form.title("Esse é o título") 		#Insere um título
form.geometry("500x200+200+200")	#LarguraxAltura+X+Y
form.resizable(True, True)			#Permitir redimensionamento manual (X,Y)
form.minsize(500,200)				#mínimo redimensionamento
form.maxsize(700,300)				#máximo redimensionamento
form.attributes('-zoomed',True)		#executa o programa em tela cheia
#form.attributes('-fullscreen',True)	#permite executar usando a tela toda

form.mainloop() 					#método principal

