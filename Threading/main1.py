# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#25/11/2020
#Exemplo com threading
#para executar: $ python main.py

import threading
import time
 
def thread1(message):
    for i in range(5):
        print(message)
        time.sleep(1)

def thread2(message):
    for i in range(5):
        print(message)
        time.sleep(1)        
 
#Cria a thread1
t1 = threading.Thread(target=thread1 ,args=("Thread1 sendo executada",))

#Cria a thread2
t2 = threading.Thread(target=thread2 ,args=("Thread2 sendo executada",))

#Starta a thread1
t1.start()

#Starta a thread2
t2.start()

#Aguardando a thread ser executada 
while t1.is_alive() and t2.is_alive():
    print("Aguardandos threads serem executadas")
    time.sleep(5)
 
#Acabou a thread
print("As Threads morreram")
print("Finalizando programa")