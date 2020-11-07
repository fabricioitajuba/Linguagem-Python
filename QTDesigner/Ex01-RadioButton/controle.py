from PyQt5 import uic,QtWidgets

def funcao_principal():
    #print("teste")
    if formulario.radioButton.isChecked():
        opcao = "Opção 1 selecionada"
    elif formulario.radioButton_2.isChecked():
        opcao = "Opção 2 selecionada"
    elif formulario.radioButton_3.isChecked():
        opcao = "Opção 3 selecionada"
    elif formulario.radioButton_4.isChecked():
        opcao = "Opção 4 selecionada"
    else:
        opcao = ""

    formulario.label_2.setText(opcao)

app=QtWidgets.QApplication([])
formulario=uic.loadUi("janela.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()
