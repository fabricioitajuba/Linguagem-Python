'''
Created on Jun 25, 2016

@author: billal begueradj
'''

from tkinter import *
from tkinter import ttk


def removeLabel(var):
    global frames
    z = -1
    # Loop over the list of rames
    for frame in frames:
        z = z + 1
        # Check the text variable of the label of this frame
        if frame.winfo_children()[0].var == var:
           # Destroy the related frame
           frame.destroy()
           # Update the size of the list of frames
           frames = frames[:z] + frames[z+1:]
           # Do not forget to always rest this flag back to -1
           z = -1 

    # Update the labels' numbers       
    r = 0
    for frame in frames:
        frame.winfo_children()[0].var.set(r)
        r = r + 1


def addNewLabel():
    global  frames, i
    var = IntVar()
    frame = Frame(root)
    i = i + 1
    frame.grid(row=i, column=0)    
    var.set(len(frames))
    l = ttk.Label(frame, textvariable=var)
    l.grid(row=0, column=0)
    l.var = var
    b = ttk.Button(frame, text="Remove", command=lambda: removeLabel(var))    
    b.grid(row=0, column=1)
    frames.append(frame)


if __name__ == '__main__':
   root = Tk()
   frames = []
   i = 1
   ttk.Button(root, text="add label", command=addNewLabel).grid(column=0, row=0)
   root.mainloop()