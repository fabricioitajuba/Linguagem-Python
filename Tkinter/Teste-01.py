# -*- coding: utf-8 -*-
from Tkinter import *
        
janela = Tk()
janela.configure(bg='light blue1')
janela.title('jogo da velha')
janela.overrideredirect(True)
janela.geometry("{0}x{1}+0+0".format(janela.winfo_screenwidth(), janela.winfo_screenheight()))

def sair():
    janela.destroy()

def maxmize():
    janela.geometry("{0}x{1}+0+0".format(janela.winfo_screenwidth(), janela.winfo_screenheight()))
    janela.overrideredirect(True)

def abas():
    janela.overrideredirect(False)

bt = Button(width=20, bg='red',font='roboto',text='fechar janela',command=sair)
bt.place(x=0,y=0)

bt = Button(width=20, bg='light blue',font='roboto',text='mostrar como tela cheia',command=maxmize)
bt.place(x=190,y=0)

bt = Button(width=20, bg='light blue',font='roboto',text='mostrar como janela',command=abas)
bt.place(x=380,y=0)
