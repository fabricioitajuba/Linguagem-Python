from tkinter import *

form = Tk()

form.title("Label Frame")
form.geometry("500x300")

lb_esportes = LabelFrame(form, text = "Esportes", borderwidth = 1, relief = "solid")
lb_esportes.place(x=10, y=10, width=300, height=100)

le1 = Label(lb_esportes, text="Futebol")
le1.pack()

le2 = Label(lb_esportes, text="Tênis")
le2.pack()

le3 = Label(lb_esportes, text="Handeboll")
le3.pack()

form.mainloop()