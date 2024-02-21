from PyQt5 import uic, QtWidgets
import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'pmysql',
    password = 'Senha@123',
    database = 'CONTROLE_DE_ESTOQUE'
)

def listarCadastro():
    listarCadastro.show()
    cursor = conexao.cursor()
    comandoSqlListar = 'SELECT * FROM cadastro_de_produtos'
    cursor.execute(comandoSqlListar)
    leituraBanco = cursor.fetchall()
    
    listarCadastro.tableWidget.setRowCount(len(leituraBanco))
    listarCadastro.tableWidget.setColumnCount(4)
    
    for linhas in range(0, len(leituraBanco)):
        for colunas in range(0, 4):
            listarCadastro.tableWidget.setItem(linhas, colunas, QtWidgets.QTableWidgetItem(str(leituraBanco[linhas][colunas])))

def cadastroProduto():
    produto = formulario.txtProduto.text()
    preco = formulario.txtPreco.text()
    quantidade = formulario.txtQuantidade.text()

    cursor = conexao.cursor()
    comandoSqlCadastro = 'INSERT INTO cadastro_de_produtos (produto, preco, quantidade) VALUES (%s, %s, %s)'
    dados = (str(produto), str(preco), str(quantidade))

    cursor.execute(comandoSqlCadastro, dados)
    conexao.commit()
    
    formulario.txtProduto.setText('')
    formulario.txtPreco.setText('')
    formulario.txtQuantidade.setText('')
    formulario.labelConfirmacaoInTela.setText('PRODUTO CADASTRADO COM SUCESSO')

app = QtWidgets.QApplication([])
formulario=uic.loadUi('/home/dgutierres/projects-python/py_pmysql/apps/controleEstoque/front/telaFormulario.ui')
formulario.buttonCadastrar.clicked.connect(cadastroProduto)

from relatorio import relatorio
formulario.buttonRelatorio.clicked.connect(listarCadastro)
listarCadastro = relatorio

formulario.show()
app.exec()
