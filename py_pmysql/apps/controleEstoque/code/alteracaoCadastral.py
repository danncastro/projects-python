from PyQt5 import uic, QtWidgets

app = QtWidgets.QApplication([])
alteracaoCadastral = uic.loadUi('/home/dgutierres/projects-python/py_pmysql/apps/controleEstoque/front/telaAlteracaoCadastral.ui')

alteracaoCadastral.show()
app.exec()
