# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#08/11/2020
#Conversão de Fahrenheit para Celsius
#para executar: $ python Teste-02.py

from Tkinter import * 					#importação da classe

#---------------------------------------------------------
# Funções
# C = (F-32) * 5/9
def calcular():
	F = float(textbox1.get())
	C = (F-32) * 5/9
	final.set(str(round(C,1)) + " graus Celsius")

#---------------------------------------------------------
# GUI
form = Tk() 							#método construdor
form.title("Fahrenheit para Celsius") 	#Insere um título

final = StringVar()

#---------------------------------------------------------
# widgets
label1 = Label(form, text = "Graus Fahrenheit")
textbox1 = Entry(form)
button1 = Button(form, text = "Calcular", command = calcular)
label_resultado = Label(form, textvariable = final)

#---------------------------------------------------------
# layout
label1.grid()
textbox1.grid()
button1.grid()
label_resultado.grid()

form.mainloop() 						#método principal

