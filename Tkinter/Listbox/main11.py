# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#21/11/2020
#Listbox
#para executar: $ python main11.py

from tkinter import Tk, OptionMenu, IntVar
root = Tk()
variative = IntVar()        
option_list = [1,2,3,4]
variative.set('Select')

def background(sel):
    if sel == 1:
        root.config(bg='red')
    elif sel == 2:
        root.config(bg='yellow')
    elif sel == 3:
        root.config(bg='gray')
    elif sel == 4:
        root.config(bg='green')   

listbox = OptionMenu(root,variative, *option_list, command=background)
listbox.pack()
root.mainloop()