"""


    developed by richartzCoffee
"""


import sqlite3
from collections import namedtuple

Database_file = r'database\DatabasePool.db' # path to the Database_file  -> you must not change


class Database:

    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file)
        self.manipulate_Database = self.conn.cursor()

    def commit(self):
        if self.conn:
            self.conn.commit()

    def manipulate_database(self  , manipulate):
        if self.conn:
            self.manipulate_Database.execute(f'''{manipulate}''')
            self.conn.commit()

    def return_database(self):
        if self.conn:
            return self.manipulate_Database.fetchall()

    def close_database(self):
        if self.conn:
            self.conn.close()


class User:

    def __init__(self, database_file=r'DatabasePool.db'):
        self.database_user = Database(database_file)
        self.database_user.manipulate_database("""
        CREATE TABLE IF NOT EXISTS users(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                cpf VARCHAR(11) NOT NULL,
                password TEXT NOT NULL,
                accessType BIT NOT NULL,
                adm BIT NOT NULL
        )
        """)

    def manipulate_table_user(self, manipulate):

        if self.database_user:
            self.database_user.manipulate_database(manipulate)
            return True

        return False

    def add_user(self, name, password, cpf, type_access=0, admin=0):

        self.database_user.manipulate_database(f'''
        INSERT INTO users (name,cpf,password,accessType,adm)
        VALUES ('{name}','{cpf}','{password}',{type_access},{admin});
        ''')

    def find_name(self, name):

        self.database_user.manipulate_database(f'''
            SELECT * FROM users WHERE name='{name}'
            ''')
        return return_treatment_list_of_tuple_users(self.database_user.return_database())

    def find_cpf(self, cpf):

        self.database_user.manipulate_database(f'''
            SELECT * FROM users WHERE cpf='{cpf}'
            ''')

        return return_treatment_list_of_tuple_users(self.database_user.return_database())

    def find_access(self,type_access):
        self.database_user.manipulate_database(f'''
                    SELECT * FROM users WHERE accessType='{type_access}'
                    ''')
        return return_treatment_list_of_tuple_users(self.database_user.return_database())

    def find_adm(self,adm):
        self.database_user.manipulate_database(f'''
                            SELECT * FROM users WHERE adm='{adm}'
                            ''')
        return return_treatment_list_of_tuple_users(self.database_user.return_database())

    def delete_user(self,key_table):
        self.database_user.manipulate_database(f'''
            DELETE FROM users
            WHERE id = {key_table};
            ''')

    def user_close(self):
        self.database_user.close_database()


class Device:

    def __init__(self, database_file=r'DatabasePool.db'):
        self.database_device = Database(database_file)
        self.database_device.manipulate_database("""
            CREATE TABLE IF NOT EXISTS device(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    port TEXT NOT NULL ,
                    type_of_action BIT NOT NULL,
                    status BIT NOT NULL
        
            );""")

    def manipulate_table_device(self, manipulate):
        if self.database_device:
            self.database_device.manipulate_database(manipulate)
            return True

        return False

    def add_device(self,name, port, type_of_action=0, status=0):
        self.database_device.manipulate_database(f'''
            INSERT INTO device (name,port,type_of_action,status)
            VALUES ('{name}','{port}',{type_of_action},{status})
            ''')

    def find_name(self,name):

        self.database_device.manipulate_database(f'''
        SELECT * FROM device WHERE name='{name}'
        ''')
        return return_treatment_list_of_tuple_device(self.database_device.return_database())

    def find_port(self,port):
        self.database_device.manipulate_database(f'''
            SELECT * FROM device WHERE port='{port}'
            ''')
        return return_treatment_list_of_tuple_device(self.database_device.return_database())

    def find_type_of_action(self,type_of_action):
        self.database_device.manipulate_database(f'''
            SELECT * FROM device WHERE type_of_action='{type_of_action}'
            ''')
        return return_treatment_list_of_tuple_device(self.database_device.return_database())

    def find_status(self,status):
        self.database_device.manipulate_database(f'''
         SELECT * FROM device WHERE status='{status}'
         ''')
        return return_treatment_list_of_tuple_device(self.database_device.return_database())


def treatment_for_tuple_device(entry_list):

    if len(entry_list) == 0:
        return False
    else:
        returnedDatabase_file = namedtuple('returnedDatabase_file',
                                            ['id',
                                             'name',
                                             'port',
                                             'type_of_action',
                                             'status'])

        exit_tuple = returnedDatabase_file(id=entry_list[0],
                                           name=entry_list[1],
                                           port=entry_list[2],
                                           type_of_action=entry_list[3],
                                           status=entry_list[4])

        return exit_tuple

def return_treatment_list_of_tuple_device(entry_list):

    if len(entry_list) == 0:
        return False
    else:
        exit_list = list()
        for i in entry_list:
            exit_tuple = treatment_for_tuple_device(i)
            exit_list.append(exit_tuple)

        return exit_list

def treatment_for_tuple_user(entry_list):

    if len(entry_list) == 0:
        return False
    else:
        returnedDatabase_file = namedtuple('returnedDatabase_file',
                                           ['id',
                                            'name',
                                            'cpf',
                                            'password',
                                            'access',
                                            'admin'])

        user_return = returnedDatabase_file(id=entry_list[0],
                                            name=entry_list[1],
                                            cpf=entry_list[2],
                                            password=entry_list[3],
                                            access=entry_list[4],
                                            admin=entry_list[5])

        return user_return

def return_treatment_list_of_tuple_users(entry_list):

    if len(entry_list) == 0:
        return False
    else:
        exit_list = list()
        for i in entry_list:
            exit_tuple = treatment_for_tuple_user(i)
            exit_list.append(exit_tuple)

        return exit_list

def access():
    """
    no return function.
    connect to the Database_file.
    if there is no Database_file, create a Database_file.
    disconnect Database_file
    """

    global Database_file
    conn = sqlite3.connect(Database_file)

    manipulate_database_file = conn.cursor()

    control_return = True

    try:
        manipulate_database_file.execute("""
        CREATE TABLE IF NOT EXISTS users(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                cpf VARCHAR(11) NOT NULL,
                password TEXT NOT NULL,
                accessType BIT NOT NULL,
                adm BIT NOT NULL
        );
        """)
        manipulate_database_file.execute("""
        CREATE TABLE IF NOT EXISTS device(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                port TEXT NOT NULL ,
                type_of_action BIT NOT NULL,
                status BIT NOT NULL

            );""")

        manipulate_database_file.execute("""

        CREATE TABLE IF NOT EXISTS scenes(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date_of_start DATE NOT NULL,
                date_of_finish DATE NOT NULL,
                hour_of_start TIME NOT NULL,
                timer TIME NOT NULL,
                status BIT NOT NULL,
                statusLuzes BIT NOT NULL,
                repestirSemana BIT NOT NULL 

        );
        """)
    except sqlite3.OperationalError:

        control_return = False

    finally:

        conn.close()

    return control_return

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
    global Database_file
    conn = sqlite3.connect(Database_file)
    manipulate_Database_file = conn.cursor()

    manipulate_Database_file.execute(f'''
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

    global Database_file
    conn = sqlite3.connect(Database_file)
    manipulate_Database_file = conn.cursor()

    manipulate_Database_file.execute(f'''
    SELECT * FROM users WHERE name='{name}'
    ''')
    list_user = manipulate_Database_file.fetchall()

    if (len(list_user) == 0):
        conn.close()
        return False
    else:
        returnedDatabase_file = namedtuple('returnedDatabase_file',['id', 'name', 'cpf', 'password', 'access', 'admin'])
        user_return = returnedDatabase_file(id=list_user[0][0],
                                       name=list_user[0][1],
                                       cpf=list_user[0][2],
                                       password=list_user[0][3],
                                       access=list_user[0][4],
                                       admin=list_user[0][5])
        conn.close()
        return user_return

def find_user_cpf(cpf):

    global Database_file
    conn = sqlite3.connect(Database_file)
    manipulate_Database_file = conn.cursor()

    manipulate_Database_file.execute(f'''
    SELECT * FROM users WHERE cpf='{cpf}'
    ''')
    list_user = manipulate_Database_file.fetchall()

    if (len(list_user) == 0):
        conn.close()
        return False
    else:
        returnedDatabase_file = namedtuple('returnedDatabase_file', ['id', 'name', 'cpf', 'password', 'access', 'admin'])

        user_return = returnedDatabase_file(id=list_user[0][0],
                                       name=list_user[0][1],
                                       cpf=list_user[0][2],
                                       password=list_user[0][3],
                                       access=list_user[0][4],
                                       admin=list_user[0][5])
        conn.close()
        return user_return

def find_user_access(access_type):
    global Database_file
    conn = sqlite3.connect(Database_file)
    manipulate_Database_file = conn.cursor()

    manipulate_Database_file.execute(f'''
        SELECT * FROM users WHERE access='{access_type}'
        ''')
    list_user = manipulate_Database_file.fetchall()

    if (len(list_user) == 0):
        conn.close()
        return False
    else:
        returnedDatabase_file = namedtuple('returnedDatabase_file', ['id', 'name', 'cpf', 'password', 'access', 'admin'])
        user_return = returnedDatabase_file(id=list_user[0][0],
                                       name=list_user[0][1],
                                       cpf=list_user[0][2],
                                       password=list_user[0][3],
                                       access=list_user[0][4],
                                       admin=list_user[0][5])
        conn.close()
        return user_return

def find_user_adm(adm):
    global Database_file
    conn = sqlite3.connect(Database_file)
    manipulate_Database_file = conn.cursor()

    manipulate_Database_file.execute(f'''
        SELECT * FROM users WHERE adm='{adm}'
        ''')
    list_user = manipulate_Database_file.fetchall()

    if (len(list_user) == 0):
        conn.close()
        return False
    else:
        returnedDatabase_file = namedtuple('returnedDatabase_file', ['iduser', 'name', 'cpf', 'password', 'access', 'admin'])
        user_return = returnedDatabase_file(iduser=list_user[0][0],
                                       name=list_user[0][1],
                                       cpf=list_user[0][2],
                                       password=list_user[0][3],
                                       access=list_user[0][4],
                                       admin=list_user[0][5])
        conn.close()
        return user_return

def delete_user(key_table):
    global Database_file
    conn = sqlite3.connect(Database_file)
    manipulate_Database_file = conn.cursor()

    manipulate_Database_file.execute(f'''
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


#type_of_action

def add_table_device(name, port, type_of_action=0, status=0):
    """

    :param name: device name
    :param port: network port for communication
    :param type_of_action: type of type_of_action lamp/motor
    :param status: currente status, on = 1 / off = 0
    :return: there is not return

    developed by richartzCoffee
    """

    global Database_file

    conn = sqlite3.connect(Database_file)        #connect to the Database_file
    manipulate_Database_file = conn.cursor()

    # manipulate Database_file
    manipulate_Database_file.execute(f'''
    INSERT INTO dispositivos (name,port,type_of_action,status)
    VALUES ('{name}','{port}',{type_of_action},{status})
    ''')
    conn.commit()
    conn.close()


def find_device_name(name):

    global Database_file
    conn = sqlite3.connect(Database_file)
    manipulate_Database_file = conn.cursor()

    manipulate_Database_file.execute(f'''
    SELECT * FROM device WHERE name='{name}'
    ''')
    list_user = manipulate_Database_file.fetchall()

    if len(list_user) == 0:
        conn.close()
        return False
    else:
        returnedDatabase_file = namedtuple('returnedDatabase_file', ['id', 'name', 'port', 'type_of_action', 'status'])

        user_return = returnedDatabase_file(id=list_user[0][0],
                                       name=list_user[0][1],
                                       port=list_user[0][2],
                                       type_of_action=list_user[0][3],
                                       status=list_user[0][4])
        conn.close()
        return user_return


def find_device_port(port):

    global Database_file
    conn = sqlite3.connect(Database_file)
    manipulate_Database_file = conn.cursor()

    manipulate_Database_file.execute(f'''
    SELECT * FROM device WHERE port='{port}'
    ''')
    list_user = manipulate_Database_file.fetchall()

    if (len(list_user) == 0):
        conn.close()
        return False
    else:
        returnedDatabase_file = namedtuple('returnedDatabase_file',['id', 'name', 'port', 'type_of_action', 'status'])

        user_return = returnedDatabase_file(id=list_user[0][0],
                                       name=list_user[0][1],
                                       port=list_user[0][2],
                                       type_of_action=list_user[0][3],
                                       status=list_user[0][4])

        conn.close()
        return user_return


def find_device_type_of_action(type_of_action):
    global Database_file
    conn = sqlite3.connect(Database_file)
    manipulate_Database_file = conn.cursor()

    manipulate_Database_file.execute(f'''
    SELECT * FROM device WHERE type_of_action='{type_of_action}'
    ''')
    list_user = manipulate_Database_file.fetchall()

    if (len(list_user) == 0):
        conn.close()
        return False
    else:
        returnedDatabase_file = namedtuple('returnedDatabase_file', ['id', 'name', 'port', 'type_of_action', 'status'])

        user_return = returnedDatabase_file(id=list_user[0][0],
                                       name=list_user[0][1],
                                       port=list_user[0][2],
                                       type_of_action=list_user[0][3],
                                       status=list_user[0][4])

        conn.close()
        return user_return


def find_device_status(status):
    global Database_file
    conn = sqlite3.connect(Database_file)
    manipulate_Database_file = conn.cursor()

    manipulate_Database_file.execute(f'''
    SELECT * FROM device WHERE status='{status}'
    ''')
    list_user = manipulate_Database_file.fetchall()

    if (len(list_user) == 0):
        conn.close()
        return False
    else:
        returnedDatabase_file = namedtuple('returnedDatabase_file', ['id', 'name', 'port', 'type_of_action', 'status'])

        user_return = returnedDatabase_file(id=list_user[0][0],
                                       name=list_user[0][1],
                                       port=list_user[0][2],
                                       type_of_action=list_user[0][3],
                                       status=list_user[0][4])

        conn.close()
        return user_return


def delete_devise(key_table):
    global Database_file
    conn = sqlite3.connect(Database_file)
    manipulate_Database_file = conn.cursor()

    manipulate_Database_file.execute(f'''
    DELETE FROM device
    WHERE id = {key_table}
    ''')

    conn.commit()

    conn.close()
