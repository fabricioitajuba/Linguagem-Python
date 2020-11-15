Este programa envia um dado pela serial e recebe outro

Conectar o arduino em sua IDE e descobrir em qual serial o mesmo se encontra.

Caso esteja utilizando o Linux e não consiga fazer a comunicação pela serial, execute a seguinte linha de comando:

sudo chmod 777 "caminho da porta serial"

Ex:
$ sudo chmod 777 /dev/ttyACM0


Caso não tenha a biblioteca pyserial instalada, instale através do seguinte comando (se estiver utilizando o python 3):

$ pip3 install pyserial
