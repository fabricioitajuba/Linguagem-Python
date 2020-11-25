from tkinter import *

Window = Tk()

def Open():
    New_Window = Tk()
    #You can edit here.
    New_Window.mainloop()

bt = Button(Window, text="Open", command=Open)
bt.pack()

Window.mainloop()
