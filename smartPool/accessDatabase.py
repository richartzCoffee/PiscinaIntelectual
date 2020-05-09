"""


    developed by richartzCoffee
"""

import sqlite3
from collections import namedtuple

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

    control_return = True

    try:
        manipulateDatabase.execute("""
        CREATE TABLE users(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                cpf VARCHAR(11) NOT NULL,
                password TEXT NOT NULL,
                accessType BIT NOT NULL,
                adm BIT NOT NULL
        );
        """)
        manipulateDatabase.execute("""
        CREATE TABLE device(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                port TEXT NOT NULL ,
                drive BIT NOT NULL,
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
    except sqlite3.OperationalError:

        control_return = False

    finally:

        conn.close()

    return control_return


#user roles


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
    INSERT INTO users (name,cpf,password,accessType,adm)
    VALUES ('{name}','{cpf}','{password}',{type_access},{admin});
    ''')
    conn.commit()
    conn.close()


def find_user_name(name):
    """

    :param name:
    :return:

    developed by richartzCoffee
    """

    global DATABASE
    conn = sqlite3.connect(DATABASE)
    manipulateDatabase = conn.cursor()

    manipulateDatabase.execute(f'''
    SELECT * FROM users WHERE name='{name}'
    ''')
    list_user = manipulateDatabase.fetchall()

    if (len(list_user) == 0):
        conn.close()
        return False
    else:
        returnedDatabase = namedtuple('returnedDatabase',['id', 'name', 'cpf', 'password', 'access', 'admin'])
        user_return = returnedDatabase(id=list_user[0][0],
                                       name=list_user[0][1],
                                       cpf=list_user[0][2],
                                       password=list_user[0][3],
                                       access=list_user[0][4],
                                       admin=list_user[0][5])
        conn.close()
        return user_return


def find_user_cpf(cpf):

    global DATABASE
    conn = sqlite3.connect(DATABASE)
    manipulateDatabase = conn.cursor()

    manipulateDatabase.execute(f'''
    SELECT * FROM users WHERE cpf='{cpf}'
    ''')
    list_user = manipulateDatabase.fetchall()

    if (len(list_user) == 0):
        conn.close()
        return False
    else:
        returnedDatabase = namedtuple('returnedDatabase', ['id', 'name', 'cpf', 'password', 'access', 'admin'])

        user_return = returnedDatabase(id=list_user[0][0],
                                       name=list_user[0][1],
                                       cpf=list_user[0][2],
                                       password=list_user[0][3],
                                       access=list_user[0][4],
                                       admin=list_user[0][5])
        conn.close()
        return user_return


def find_user_access(access_type):
    global DATABASE
    conn = sqlite3.connect(DATABASE)
    manipulateDatabase = conn.cursor()

    manipulateDatabase.execute(f'''
        SELECT * FROM users WHERE access='{access_type}'
        ''')
    list_user = manipulateDatabase.fetchall()

    if (len(list_user) == 0):
        conn.close()
        return False
    else:
        returnedDatabase = namedtuple('returnedDatabase', ['id', 'name', 'cpf', 'password', 'access', 'admin'])
        user_return = returnedDatabase(id=list_user[0][0],
                                       name=list_user[0][1],
                                       cpf=list_user[0][2],
                                       password=list_user[0][3],
                                       access=list_user[0][4],
                                       admin=list_user[0][5])
        conn.close()
        return user_return


def find_user_adm(adm):
    global DATABASE
    conn = sqlite3.connect(DATABASE)
    manipulateDatabase = conn.cursor()

    manipulateDatabase.execute(f'''
        SELECT * FROM users WHERE adm='{adm}'
        ''')
    list_user = manipulateDatabase.fetchall()

    if (len(list_user) == 0):
        conn.close()
        return False
    else:
        returnedDatabase = namedtuple('returnedDatabase', ['iduser', 'name', 'cpf', 'password', 'access', 'admin'])
        user_return = returnedDatabase(iduser=list_user[0][0],
                                       name=list_user[0][1],
                                       cpf=list_user[0][2],
                                       password=list_user[0][3],
                                       access=list_user[0][4],
                                       admin=list_user[0][5])
        conn.close()
        return user_return


def delete_user(key_table):
    global DATABASE
    conn = sqlite3.connect(DATABASE)
    manipulateDatabase = conn.cursor()

    manipulateDatabase.execute(f'''
    DELETE FROM users
    WHERE id = {key_table}
    ''')

    conn.commit()

    conn.close()



'''
-------------------------------------
            device roles
-------------------------------------
'''


def add_table_device(name, port, drive=0, status=0):
    """

    :param name: device name
    :param port: network port for communication
    :param drive: type of drive lamp/motor
    :param status: currente status, on = 1 / off = 0
    :return: there is not return

    developed by richartzCoffee
    """

    global DATABASE

    conn = sqlite3.connect(DATABASE)        #connect to the database
    manipulateDatabase = conn.cursor()

    # manipulate database
    manipulateDatabase.execute(f'''
    INSERT INTO dispositivos (nomeDispositivos,portaDispositivo,acionamento,status)
    VALUES ('{name}','{port}',{drive},{status})
    ''')
    conn.commit()
    conn.close()


def find_device_name(name):

    global DATABASE
    conn = sqlite3.connect(DATABASE)
    manipulateDatabase = conn.cursor()

    manipulateDatabase.execute(f'''
    SELECT * FROM device WHERE name='{name}'
    ''')
    list_user = manipulateDatabase.fetchall()

    if (len(list_user) == 0):
        conn.close()
        return False
    else:
        returnedDatabase = namedtuple('returnedDatabase', ['id', 'name', 'port', 'drive', 'status'])

        user_return = returnedDatabase(id=list_user[0][0],
                                       name=list_user[0][1],
                                       port=list_user[0][2],
                                       drive=list_user[0][3],
                                       status=list_user[0][4])
        conn.close()
        return user_return


def find_device_port(port):

    global DATABASE
    conn = sqlite3.connect(DATABASE)
    manipulateDatabase = conn.cursor()

    manipulateDatabase.execute(f'''
    SELECT * FROM device WHERE port='{port}'
    ''')
    list_user = manipulateDatabase.fetchall()

    if (len(list_user) == 0):
        conn.close()
        return False
    else:
        returnedDatabase = namedtuple('returnedDatabase',['id', 'name', 'port', 'drive', 'status'])

        user_return = returnedDatabase(id=list_user[0][0],
                                       name=list_user[0][1],
                                       port=list_user[0][2],
                                       drive=list_user[0][3],
                                       status=list_user[0][4])

        conn.close()
        return user_return


def find_device_drive(drive):
    global DATABASE
    conn = sqlite3.connect(DATABASE)
    manipulateDatabase = conn.cursor()

    manipulateDatabase.execute(f'''
    SELECT * FROM device WHERE drive='{drive}'
    ''')
    list_user = manipulateDatabase.fetchall()

    if (len(list_user) == 0):
        conn.close()
        return False
    else:
        returnedDatabase = namedtuple('returnedDatabase', ['id', 'name', 'port', 'drive', 'status'])

        user_return = returnedDatabase(id=list_user[0][0],
                                       name=list_user[0][1],
                                       port=list_user[0][2],
                                       drive=list_user[0][3],
                                       status=list_user[0][4])

        conn.close()
        return user_return


def find_device_status(status):
    global DATABASE
    conn = sqlite3.connect(DATABASE)
    manipulateDatabase = conn.cursor()

    manipulateDatabase.execute(f'''
    SELECT * FROM device WHERE status='{status}'
    ''')
    list_user = manipulateDatabase.fetchall()

    if (len(list_user) == 0):
        conn.close()
        return False
    else:
        returnedDatabase = namedtuple('returnedDatabase', ['id', 'name', 'port', 'drive', 'status'])

        user_return = returnedDatabase(id=list_user[0][0],
                                       name=list_user[0][1],
                                       port=list_user[0][2],
                                       drive=list_user[0][3],
                                       status=list_user[0][4])

        conn.close()
        return user_return


def delete_devise(key_table):
    global DATABASE
    conn = sqlite3.connect(DATABASE)
    manipulateDatabase = conn.cursor()

    manipulateDatabase.execute(f'''
    DELETE FROM device
    WHERE id = {key_table}
    ''')

    conn.commit()

    conn.close()