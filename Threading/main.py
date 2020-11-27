# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#25/11/2020
#Exemplo com threading
#para executar: $ python main.py

import threading
import time
 
def worker(message):
    for i in range(5):
        print(message)
        time.sleep(1)
 
#Cria a thread
t = threading.Thread(target=worker,args=("Thread sendo executada",))

#Starta a thread
t.start()

#Aguardando a thread ser executada 
while t.is_alive():
    print("Aguardando thread")
    time.sleep(5)
 
#Acabou a thread
print("Thread morreu")
print("Finalizando programa")