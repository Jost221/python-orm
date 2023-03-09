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