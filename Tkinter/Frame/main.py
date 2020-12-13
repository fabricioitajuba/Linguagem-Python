# -*- coding: utf-8 -*-
#Fabricio de Lima Ribeiro
#12/11/2020
#Exemplo de uso do frame
#para executar: $ python3 main.py

from tkinter import *

form = Tk()
form.title("Exemplo de uso do frame")
form.geometry("500x300")

#relief (flat, raised, sunken, solid)
frame1 = Frame(form, borderwidth=3, relief="solid")
frame1.place(x=10, y=10, width=300, height=100)

frame2 = Frame(form, borderwidth=1, relief="sunken")
frame2.place(x=10, y=150, width=300, height=100)

frame3 = Frame(form, borderwidth=1, relief="sunken", bg="#008")
frame3.place(x=350, y=150, width=100, height=100)

label1 = Label(frame1, text="Texto 1").pack()
label2 = Label(frame2, text="Texto 2").pack()
label3 = Label(frame3, text="Texto 3")
label3.place(x=20, y=40)

form.mainloop()