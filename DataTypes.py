class DataType:
    def __init__(self, size=0, nullable=False, default=None, primary_key=False):
        self.size = None
        self.nullable = None
        self.default = None
        self.unique = None
        self.check = None
        self.primary_key = None
        self.foreign_key = None

class String(DataType):
    name = "TEXT"

class Integer(DataType):
    name = "INTEGER"
    def __init__(self, auto_increment:bool=False):
        super().__init__()
        self.autoincrement=auto_increment

class Data(DataType):
    name = "DATA"

class Float(DataType):
    name = "FLOAT"

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