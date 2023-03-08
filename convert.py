import models
from DataTypes import *
import inspect

class emptiness:
    pass

request = ''

def for_size(content, request):
    try:
        if content.size:
            request+=f'({content.size})'
        return ['ok', request]
    except Exception as ex:
        return ['error', ex] 
            
def for_pk(content, request):
    try:
        if content.pk:
            request+=f'PRIMARY KEY '
        return ['ok', request]
    except Exception as ex:
        return ['error', ex]

def for_null(content, request):
    try:
        if content.nullable:
            request+=f'NOT NULL '
        return ['ok', request]
    except Exception as ex:
        return ['error', ex]
    
def for_auto_increment(content, request):
    try:
        if content.auto_increment:
            request+=f'AUTO_INCREMENT '
        return ['ok', request]
    except Exception as ex:
        return ['error', ex]
    
def for_unique(content, request):
    try:
        if content.unique:
            request+=f'UNIQUE '
        return ['ok', request]
    except Exception as ex:
        return ['error', ex]
    
def for_default(content, request):
    try:
        if content.default:
            request+=f'DEFAULT {content.default}'
        return ['ok', request]
    except Exception as ex:
        return ['error', ex]
    
def for_check(content, request):
    try:
        if content.check:
            request+=f'CHECK {content.check} '
        return ['ok', request]
    except Exception as ex:
        return ['error', ex]

CHECKS = [for_size, for_pk, for_null, for_auto_increment, for_unique, for_default, for_check]


def get_atr(table_name: str, table: dict):
    returned = f'CREATE TABLE IF NOT EXISTS {table_name}('
    for column, info_column in table.items():
        if info_column.__class__.__weakref__.__objclass__ == DataType:
            returned+=f'{column} {info_column.name} '
            for check in CHECKS:
                res = check(info_column, returned)
                if res[0] == 'ok':
                    returned = res[1]
            returned +='\x08,'
            # returned+=','
    returned+='\x08)'
    return returned



for mod_name, value in models.__dict__.items():
    if hasattr(value, '__module__') and value.__module__ == 'models':
        table_name = mod_name
        mod = dict(value.__dict__)
        for i in emptiness.__dict__:
            mod.pop(i)
        request+= get_atr(table_name, mod)
        request+='\n'
print(request)