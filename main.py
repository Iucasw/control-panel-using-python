from PyQt5 import uic,QtWidgets

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    print('Discord: ', linha1)
    print('Produto: ', linha2)


app=QtWidgets.QApplication([])
formulario=uic.loadUi("form.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()