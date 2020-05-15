
from smartPool import accessDatabase
from smartPool import cryptographyAndValidation
from PyQt5 import uic, QtWidgets
import sys


class InterfaceForUser:
    def __init__(self):

        self.windons_login_screen = QtWidgets.QApplication(sys.argv)
        self.login_screen = uic.loadUi(r"UI\Opcoes.ui")
        self.login_screen.show()
        self.windons_login_screen.exec()


