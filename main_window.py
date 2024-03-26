from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QMessageBox
import sys



class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, *kwargs)

        #CONFIGURANDO O LAYOUT BÁSICO
        self.cw = QWidget() #criando o central widget
        self.vLayout = QVBoxLayout() #criando um layout
        self.cw.setLayout(self.vLayout) #adicionando o layout no central widget
        self.setCentralWidget(self.cw)

        self.setWindowTitle("Calculadora") #setando o titulo da janela


    def adjustFixedSize(self):
        #ÚLTIMAS COISAS A SEREM FEITAS
        self.adjustSize() #ajustar o tamanho da janela
        self.setFixedSize(self.width(), self.height()) #impede o redimensionamento da janela

    def AddWidgetToVlayout(self, widget :QWidget):
        self.vLayout.addWidget(widget)
    
    def makeMsgBox(self):
        return QMessageBox(self)
        

        