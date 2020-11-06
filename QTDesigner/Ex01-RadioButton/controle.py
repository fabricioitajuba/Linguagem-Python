from PyQt5 import uic,QtWidgets

def funcao_principal():
    print("teste")

app=QtWidgets.QApplication([])
formulario=uic.loadUi("janela.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()
