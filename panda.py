from main import *

import sys
import plyer



class MyPopup(QWidget):
    def __init__(self):
        QWidget.__init__(self)

    def paintEvent(self, e):
        dc = QPainter(self)
        dc.drawLine(0, 0, 100, 100)
        dc.drawLine(100, 0, 0, 100)


class Panda(Ui_mainwindow):
    def __init__(self, window):
        self.w = MyPopup()
        self.setupUi(window)
        self.open.clicked.connect(self.abrir)
        self.compress.clicked.connect(self.comprimir)
        self.extract.clicked.connect(self.extrair)
        self.exit.clicked.connect(self.sair)

    def abrir(self):
        file = plyer.filechooser.open_file()

        string = file[0]

        print(file, string)

        return file, string

    def comprimir(self):
        string = "lorum episodic"
        plyer.filechooser.save_file()

    def extrair(self):
        print("butao extrair pressionado")

    def sair(self, ):
        self.w.setGeometry(QRect(100, 100, 400, 200))
        self.w.setWindowTitle('Sair')
        self.w.show()
        self.exit(10)

    def _file_selection_dialog(self, **kwargs):
        raise NotImplementedError()


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Panda(MainWindow)
MainWindow.show()
app.exec_()
