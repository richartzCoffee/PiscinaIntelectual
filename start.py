'''
                            Piratas das piscinas
_________________________________________________________________________________

-Desenvolvido por   Daniel Richartz,
                    João Gustavo Bastos de Souza ,
                    Luca Alfaro Rampinelli.

Piratas das piscinas.
IFSC 04/2020

    O seguinte programa foi feito com o objetivo inicial de desenvolver um programa para
criar o acessar um banco de dados em sqlite3. Esse banco de dados tem função de gerenciar
as ações da piscina intelectual.

_________________________________________________________________________________
'''

"""
____________________________
    Funções do sistema
----------------------------

"""
'''
lista_user = []

def login_user():

    password = login_screen.lineEditPassword.text()
    name_user = login_screen.lineEditUser.text()


    if password != and name_user != :

        login_screen.lineEditPassword.clear()
        login_screen.lineEditUser.clear()
        user_actual = user.find_name(name_user)
        if user_actual:

            if cryptographyAndValidation.validation_password(user_actual[0].password, password):


                windons_login_screen.quit()
                global lista_user
                lista_user.append(user_actual[0])

'''


from smartPool import LoginInterface


from PyQt5 import uic, QtWidgets
import sys


if __name__ == '__main__':

    u = LoginInterface.WindowLogin()
    u.windon()





"""
---------------------------------------------
        declaração de objetos
---------------------------------------------
"""









