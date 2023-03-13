import os
import sqlite3

class DataType:
    def __init__(self, size=0, nullable=False, default=None, primary_key=False, foreign_key=False, check=None, unique=None):
        if primary_key and nullable:
            raise Exception("And so, are you sure you need to make a database? because what you're trying to do reminds me of self-castration. PK must not be null")
        self.size = size
        self.nullable = nullable
        self.default = default
        self.unique = unique
        self.check = check
        self.primary_key = primary_key
        self.foreign_key = foreign_key

class String(DataType):
    name = "TEXT"

class Integer(DataType):
    name = "INTEGER"
    def __init__(self, auto_increment:bool=False, size=0, nullable=False, default=None, primary_key=False, foreign_key=False):
        if default is not None and auto_increment == True:
            raise Exception("Cannot detect what you need stupid idiot. what i`m need do auto increment or set default")
        super().__init__(size, nullable, default, primary_key, foreign_key)
        self.auto_increment=auto_increment

class Data(DataType):
    name = "DATA"

class Float(DataType):
    name = "REAL"

class Boolean(DataType):
    name = "BOOLEAN"

class Time(DataType):
    name = "TIME"

class DateTime():
    name = "DATETIME"

class Binary():
    name = "BINARY"

class ForeignKey():
    name = "FOREIGN KEY"

class Table_Engine:
    def __init__(self, **qwargs):
        for k, v in qwargs.items():
            self.__setattr__(k, v)
    
    @classmethod
    def read(cls):
        conn = sqlite3.connect(os.environ.get('DATABASE_NAME'))
        cur = conn.cursor()
        request  = "SELECT * FROM " + cls.__name__ # fix this line
        cur.execute(request)
        conn.commit()
        return cur.fetchall()

    def save(self):
        conn = sqlite3.connect(os.environ.get('DATABASE_NAME'))
        cur = conn.cursor()
        try:
            request = 'INSERT INTO '+ self.__class__.__name__ + ' ('
            values = 'VALUES ('
            for k, v in self.__dict__.items():
                request+=f'{k}, '
                if v.__class__ == str:
                    values+=f'"{v}", '
                else:
                    values+=f'{v}, '
            request = request[:-2] + ')'
            values = values[:-2] + ')'
            
        except Exception as ex:
            raise Exception(f'well congratulations your father goes fucking you with a chair on the head with these words: {ex}')

if os.environ.get('DATABASE_NAME') == None:
    os.environ['DATABASE_NAME'] = 'database.db'