#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#08/11/2020
#Relógio digital
#para executar: $ python main.py

import tkinter as tk
import time as tm

def display_time():
	current_time = tm.strftime('%I:%M:%S:%p')	#12h
	#current_time = tm.strftime('%H:%M:%S')	#24h
	clock_label['text'] = current_time
	my_window.after(1000, display_time)

my_window = tk.Tk()
my_window.title('Digital Clock')
clock_label = tk.Label(my_window, font='ariel 80', bg='black', fg='red')
clock_label.grid(row=0, column=0)
display_time()
my_window.mainloop()
