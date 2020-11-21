# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#21/11/2020
#Listbox
#para executar: $ python main10.py

from tkinter import *

screen = Tk()

screen.geometry('400x400')

#Colors of a pallette
label_tk = Label(text="A list of colors:")

#Creating a List
color_box = Listbox()
color_box.insert(1,"Red")
color_box.insert(2,"Green")
color_box.insert(3,"Yellow")
color_box.insert(4,"Blue")

label_tk.pack()
color_box.pack()

screen.mainloop()