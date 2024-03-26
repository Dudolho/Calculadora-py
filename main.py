from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QIcon
import sys
from variables import WINDOW_ICON_PATH
from display import Display
from info import Info
from styles import setupTheme
from buttons import Button, ButtonsGrid

from main_window import MainWindow

if __name__ == '__main__':


    app = QApplication(sys.argv) #inicio do loop principal da janela
    setupTheme()
    window = MainWindow()

    #info
    info = Info('43 ^ 3')
    window.AddWidgetToVlayout(info)

    #display
    display = Display()
    window.AddWidgetToVlayout(display)

    #grid de botões
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)
    

    #executa tudo
    window.adjustFixedSize() #ajustando o tamanho da janela e impedindo de redimensionar
    window.show()
    app.exec() #fim do loop principal da janela