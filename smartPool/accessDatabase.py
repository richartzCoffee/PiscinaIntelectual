"""
--------------------------------------

    developed by richartzCoffee

--------------------------------------
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

    def delete_device(self,key_table):
        self.database_device.manipulate_database(f'''
        DELETE FROM device
        WHERE id = {key_table}
        ''')


class Scenes(Database):

    def __init__(self, database_file=r'DatabasePool.db'):
        self.database_scenes = Database(database_file)
        self.database_scenes.manipulate_database("""
            CREATE TABLE IF NOT EXISTS scenes(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date_of_start DATE NOT NULL,
                date_of_finish DATE NOT NULL,
                hour_of_start TIME NOT NULL,
                timer TIME NOT NULL,
                statusMotor BIT NOT NULL,
                statusLights BIT NOT NULL,
                repeat_weekly BIT NOT NULL 

            );""")
    def scenes_close(self):
        self.database_scenes.close_database()


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


