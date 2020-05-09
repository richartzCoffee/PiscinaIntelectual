


import sqlite3

DATABASE = r'database\databasePool.db' # path to the database  -> you must not change


def access():
    """
    no return function.
    connect to the database.
    if there is no database, create the database.
    disconnect database
    """

    global DATABASE
    conn = sqlite3.connect(DATABASE)

    manipulateDatabase = conn.cursor()

    try:
        manipulateDatabase.execute("""
        CREATE TABLE users(
                idUser INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf VARCHAR(11) NOT NULL,
                senha TEXT NOT NULL,
                acesso BIT NOT NULL,
                administrador BIT NOT NULL
        );
        """)
        manipulateDatabase.execute("""
        CREATE TABLE dispositivos(
                idDisp INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nomeDispositivos TEXT NOT NULL,
                portaDispositivo TEXT NOT NULL ,
                acionamento BIT NOT NULL,
                status BIT NOT NULL

            );""")

        manipulateDatabase.execute("""

        CREATE TABLE cenas(
                idCena INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                dataInicio DATE NOT NULL,
                dataFinal DATE NOT NULL,
                horaInicio TIME NOT NULL,
                temporizador TIME NOT NULL,
                statusBomba BIT NOT NULL,
                statusLuzes BIT NOT NULL,
                repestirSemana BIT NOT NULL 

        );
        """)
    except:
        print("ok")

    finally:

        conn.close()


def add_table_user(name, password, cpf, type_access=0, admin=0):
    """
    :param name:
    :param password:
    :param cpf:
    :param type_access:
    :param admin:
    :return:

    developed by richartzCoffee
    """
    global DATABASE
    conn = sqlite3.connect(DATABASE)
    manipulateDatabase = conn.cursor()

    manipulateDatabase.execute(f'''
    INSERT INTO users (nome,cpf,senha,acesso,administrador)
    VALUES ('{name}','{cpf}','{password}',{type_access},{admin});
    ''')
    conn.commit()
    conn.close()


def add_table_disp(name, port, drive=0, status=0):
    """

    :param name: device name
    :param port: network port for communication
    :param drive: type of drive lamp/motor
    :param status: currente status, on = 1 / off = 0
    :return: there is not return

    developed by richartzCoffee
    """

    global DATABASE

    conn = sqlite3.connect(DATABASE)
    manipulateDatabase = conn.cursor()

    manipulateDatabase.execute(f'''
    INSERT INTO dispositivos (nomeDispositivos,portaDispositivo,acionamento,status)
    VALUES ('{name}','{port}',{drive},{status})
    ''')
    conn.commit()
    conn.close()


#def add_table_cenas():#ainda por fazer


def find_user_name(name):
    """

    :param name:
    :return:

    developed by richartzCoffee
    """
    from collections import namedtuple
    global DATABASE
    conn = sqlite3.connect(DATABASE)
    manipulateDatabase = conn.cursor()

    manipulateDatabase.execute(f'''
    SELECT * FROM users WHERE Nome='{name}'
    ''')
    list_user = manipulateDatabase.fetchall()

    if (len(list_user) == 0):
        return False
    else:
        returnedDatabase = namedtuple('returnedDatabase',['iduser', 'name', 'cpf', 'password', 'access', 'admin'])

        user_return = returnedDatabase(iduser= list_user[0][0], name=list_user[0][1], cpf=list_user[0][2], password=list_user[0][3], access=list_user[0][4], admin=list_user[0][5])

        return user_return


