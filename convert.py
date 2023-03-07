import models
from DataTypes import *
import inspect

class emptiness:
    pass

request = ''

def get_atr(table_name: str, table: dict):
    returned = f'CREATE TABLE IF NOT EXISTS {table_name}('
    for column, info_column in table.items():
        if info_column.__class__.__weakref__.__objclass__ == DataType:
            returned+=f'{column} {info_column.name} '
            if info_column.size:
                returned+=f'({info_column.size})'
            if info_column.primary_key:
                returned+=f'PRIMARY KEY '
            if info_column.nullable:
                returned+=f'NOT NULL '
            # if info_column.autoincrement:
            #     returned+=f'AUTOINCREMENT '
            if info_column.unique:
                returned+=f'UNIQUE '
            if info_column.default:
                returned+=f'DEFAULT {info_column.default} '
            if info_column.check:
                returned+=f'CHECK {info_column.check} '
            returned+=','
    returned+=')'
    return returned



for mod_name, value in models.__dict__.items():
    if hasattr(value, '__module__') and value.__module__ == 'models':
        table_name = mod_name
        mod = dict(value.__dict__)
        for i in emptiness.__dict__:
            mod.pop(i)
        request+= get_atr(table_name, mod)
        print(request)