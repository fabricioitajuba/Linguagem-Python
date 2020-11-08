from PyQt5 import uic,QtWidgets

def funcao_principal():

	#...
	#Aqui fica o programa
	#...

app=QtWidgets.QApplication([])
formulario=uic.loadUi("janela.ui") #Formulário criado no QTDesigner
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()
