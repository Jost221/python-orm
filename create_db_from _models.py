import models
from DataTypes import *
import sqlite3

class emptiness:
    pass

def for_size(content, request):
    try:
        if content.size:
            request+=f'({content.size})'
        return ['ok', request]
    except Exception as ex:
        return ['error', ex] 
            
def for_pk(content, request):
    try:
        if content.primary_key:
            request+=f'PRIMARY KEY '
        return ['ok', request]
    except Exception as ex:
        return ['error', ex]

def for_null(content, request):
    try:
        if not content.nullable:
            request+=f'NOT NULL '
        return ['ok', request]
    except Exception as ex:
        return ['error', ex]
    
def for_auto_increment(content, request):
    try:
        if content.auto_increment:
            request+=f'AUTOINCREMENT '
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
db_name = ''

def get_atr(table_name: str, table: dict):
    returned = f'CREATE TABLE IF NOT EXISTS {table_name}('
    for column, info_column in table.items():
        try:
            if info_column.__class__.__weakref__.__objclass__ == DataType:
                returned+=f'{column} {info_column.name} '
                for check in CHECKS:
                    res = check(info_column, returned)
                    if res[0] == 'ok':
                        returned = res[1]
                returned =returned[:-1]+', '
        except:
            raise Exception("Fuck you ugly motherless. Do you understand that in file models.py you need have onli table name as class?")
        
    returned=returned[:-2]+')'
    return returned


def create_tables(path_with_name: str):
    conn = sqlite3.connect(path_with_name)
    cur = conn.cursor()
    request = ''
    for mod_name, value in models.__dict__.items():
        if hasattr(value, '__module__') and value.__module__ == 'models':
            table_name = mod_name
            mod = dict(value.__dict__)
            for i in emptiness.__dict__:
                mod.pop(i)
            request+= get_atr(table_name, mod)
            # print(request)
            cur.execute(request)
            request=''
    global db_name
    db_name = path_with_name
    conn.commit()

def write_db(table, **qwargs):
    global db_name
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    try:
        request = 'INSERT INTO '
        for mod_name, value in models.__dict__.items():
            if table == value:
                request += f'{mod_name}('
                req_val = 'VALUES('
                for k, v in qwargs.items():
                    request+=k+', '
                    if v.__class__ == str:
                        req_val+=f'\'{v}\','
                    else:
                        req_val+=f'{v},'
                request=request[:-2]+') '
                req_val=req_val[:-1]+') '
                request+=req_val
                cur.execute(request)
                conn.commit()
                return True
    except Exception as ex:
        raise Exception(f'well congratulations your father goes fucking you with a stool on the head with these words: {ex}')

def read_db(table):
    global db_name
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    try:
        request = 'INSERT INTO '
        for mod_name, value in models.__dict__.items():
            if table == value:
                pass
    except Exception as ex:
        print(ex)
        return False
        

create_tables('my_db.db')
write_db(models.a, var1='value')
write_db(models.a, var1='value1')