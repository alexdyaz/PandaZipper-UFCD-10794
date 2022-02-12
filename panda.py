import base64
import os
import zlib

import plyer
import sys

from PyQt5.QtWidgets import QFileDialog, QApplication, QMainWindow, QPushButton

from main import *


class Panda(Ui_mainwindow):
    def __init__(self, window):
        self.setupUi(window)
        self.open.clicked.connect(self.abrir)
        self.compress.clicked.connect(self.encode)
        self.extract.clicked.connect(self.decode)
        self.exit.clicked.connect(self.sair)

    def abrir(self):
        file = plyer.filechooser.open_file()

        return file

    def encode(self):
        file, check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                                  "", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
        if check:
            ficheiro = open(file, 'r')
            text = ficheiro.read()
            print(text)

            text1 = text.encode('ascii')
            base64_bytes = base64.b64encode(text1)
            encode = base64_bytes.decode('ascii')

            print(encode)

            encoded, check = QFileDialog.getSaveFileName(None, "QFileDialog getSaveFileName() Demo",
                                                         "", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
            if check:
                encoded = open(encoded, 'w')
                encoded = encoded.write(encode)
                print(encode)
                encoded.close()

            # close file

    def decode(self):
        file, check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                                  "", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
        if check:
            ficheiro = open(file, 'r')
            text = ficheiro.read()
            print(text)

            base64_bytes = text.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            decode = message_bytes.decode('ascii')

            decoded, check = QFileDialog.getSaveFileName(None, "QFileDialog getSaveFileName() Demo",
                                                     "", "All Files (*);;Python Files (*.py);;Text Files (*.txt)")
            if check:
                print(decode)
                decoded = open(decoded, 'w')
                decoded = decoded.write(decode)

                decoded.close()

    def sair(self, ):
        # self.w.setGeometry(QRect(100, 100, 400, 200))
        # self.w.setWindowTitle('Sair')
        # self.w.show()
        self.exit(5)

    # def _file_selection_dialog(self, **kwargs):
    #    raise NotImplementedError()


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Panda(MainWindow)
MainWindow.show()
app.exec_()
