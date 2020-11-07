# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#07/11/2020
#Associando um botão
#para executar: $ python Exp-05.py

from Tkinter import * 				#importação da classe

form = Tk() 						#método construdor

form.title("Esse é o título") 		#Título do formulário
form.geometry("500x200+200+200")	#Dimensionamento do formulário

#método para tratar o botão
def cmd_Click(msg):
	print(msg)

#botao1
cmd1 = Button(form, text="Msg1", command=lambda: cmd_Click("Menssagem1"))
cmd1.pack()

#botao2
cmd2 = Button(form, text="Msg2", command=lambda: cmd_Click("Menssagem2"))
cmd2.pack()

form.mainloop() 					#método principal

