from main import *

import sys


class Panda(Ui_mainwindow):
    def __init__(self, window):
        self.setupUi(window)
        self.open.clicked.connect(self.abrir)
        self.compress.clicked.connect(self.comprimir)
        self.extract.clicked.connect(self.extrair)
        self.exit.clicked.connect(self.sair)

    def abrir(self):
        print("butao abrir pressionado")

    def comprimir(self):
        print("butao comprimir pressionado")

    def extrair(self):
        print("butao extrair pressionado")

    def sair(self):
        print("butao sair pressionado")


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Panda(MainWindow)
MainWindow.show()
app.exec_()
