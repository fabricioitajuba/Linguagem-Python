# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#07/11/2020
#Dimensionamento
#para executar: $ python main03.py

from Tkinter import * 				#importação da classe

form = Tk() 						#método construdor

form.title("Esse é o título") 		#Insere um título
form.geometry("500x200+200+200")	#LarguraxAltura+X+Y
form.resizable(False, False)		#Permitir redimensionamento manual (X,Y)

form.mainloop() 					#método principal

