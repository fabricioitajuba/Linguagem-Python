# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#08/11/2020
#Soma entre 2 números
#para executar: $ python main.py

from tkinter import * 					#importação da classe

#---------------------------------------------------------
# Funções
# C = (F-32) * 5/9
def calcular():
	A = int(textbox1.get())
	B = int(textbox2.get())
	C = A + B
	resultado.set(str(C))

#---------------------------------------------------------
# GUI
form = Tk() 							#método construdor
form.title("Soma entre dois números") 	#Insere um título
form.geometry("400x100+100+100")		#LarguraxAltura+X+Y
form.resizable(False, False)			#Permitir redimensionamento manual (X,Y)

resultado = StringVar()

#---------------------------------------------------------
# widgets
label1 = Label(form, text = "Entre com o valor de A: ")

v1 = StringVar(form, value='0')
textbox1 = Entry(form, textvariable = v1, justify='center')

label2 = Label(form, text = "Entre com o valor de B: ")

v2 = StringVar(form, value='0')
textbox2 = Entry(form, textvariable = v2, justify='center')

button1 = Button(form, text = "Calcular", command = calcular)

label3 = Label(form, text = "O valor de A+B= ")

label_resultado = Label(form, textvariable = resultado, anchor="w")

#---------------------------------------------------------
# layout

label1.config(font=("Arial", 15))
label1.grid(row = 0, column = 0)

textbox1.config(width = 5)
textbox1.grid(row = 0, column = 1)

label2.config(font=("Arial", 15))
label2.grid(row = 1, column = 0)

textbox2.config(width = 5)
textbox2.grid(row = 1, column = 1)

button1.grid(row = 1, column = 3)

label3.config(font=("Arial", 15))
label3.grid(row = 2, column = 0, sticky=E)

label_resultado.config(width = 5, font=("Arial", 15))
label_resultado.grid(row = 2, column = 1)

form.mainloop() 						#método principal

