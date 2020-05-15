
from smartPool import accessDatabase
from smartPool import cryptographyAndValidation
from PyQt5 import uic, QtWidgets
from smartPool import UserInteface
import sys


class WindowLogin:

    def __init__(self):

        self.user = accessDatabase.User()
        self.user_return = []
        self.windons_login_screen = QtWidgets.QApplication(sys.argv)
        self.login_screen = uic.loadUi(r"UI\Login.ui")
        self.check = False

    def windon(self):
        self.login_screen.show()
        self.login_screen.pushButtonLogin.clicked.connect(self.check_user)

        self.windons_login_screen.exec()
        if self.check:
            UserInteface.InterfaceForUser()


    def check_user(self):

        name = self.login_screen.lineEditUser.text().strip()
        password_test = self.login_screen.lineEditPassword.text().strip()

        self.login_screen.lineEditUser.clear()
        self.login_screen.lineEditPassword.clear()

        if name and password_test:

            self.user_return = self.user.find_name(name=name)


            if self.user_return:
                password_test = cryptographyAndValidation.cryptography_password(password_test)
                if cryptographyAndValidation.validation_password(self.user_return[0].password, password_test):

                    self.windons_login_screen.closeAllWindows()
                    exit()
                    self.check = True


                else:
                    self.login_screen.label_info.setText("Senha inválida")
            else:
                self.login_screen.label_info.setText("Usuário não encontrado")
        else:
            self.login_screen.label_info.setText("Informações incompletas")

    def interface(self):
        self.login_screen = uic.loadUi(r"UI\Opcoes.ui")
        self.login_screen.show()




