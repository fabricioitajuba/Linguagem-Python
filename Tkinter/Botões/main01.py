try:
    from tkinter import *
except:
    from Tkinter import *

# Instância
tela = Tk()

# Lista de cores que vão aparecer na paleta
cores = ["#1bbc9b","#2ecd71","#3598db","#9b58b5","#5c6d7d","#16a086","#27ae61","#2a80b9","#8f44ad","#2d3e50","#f1c40f","#e77e23","#e84c3d","#ecf0f1","#95a5a5","#f39c11","#d55401","#c1392b","#bec3c7","#7e8c8d"]

# Definição que vai apenas exibir a cor escolhida.
def clicar(btn):
   print(btn["bg"])

linha = 1
# Variável que vai andar pela lista
quantidade = 0
while linha <=4:
    coluna = 1
    while coluna<=4:
        # Atualiza dados da cor
        cor_analise = cores[quantidade]

        # Cria um botão
        btn = Button(tela,font=(" ",
        12),bg=cor_analise,fg="white",activebackground=cor_analise,highlightbackground="white",highlightthickness=1,height=1,width=3)
        btn["command"] = lambda btn=btn: clicar(btn)
        btn.grid(row=linha,column=coluna)

        # Atualiza os andantes 
        coluna=coluna+1
        quantidade = quantidade+1
    linha = linha+1

tela.mainloop()

