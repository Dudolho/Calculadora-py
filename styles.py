# QSS - Estilos do QT for Python
# https://doc.qt.io/qtforpython/tutorials/basictutorial/widgetstyling.html
# Dark Theme
# https://pyqtdarktheme.readthedocs.io/en/latest/how_to_use.html
import sys
import qdarktheme
from variables import PRIMARY_COLOR, DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR

def setupTheme():
    ...

qss = f"""
    PushButton[cssClass="specialButton"] {{
    QPushButton[cssClass="specialButton"] 
        color: #fff;
        background: {PRIMARY_COLOR};
    }}
    PushButton[cssClass="specialButton"]:hover {{
    QPushButton[cssClass="specialButton"]:hover 
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    PushButton[cssClass="specialButton"]:pressed {{
    QPushButton[cssClass="specialButton"]:pressed 
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}"""