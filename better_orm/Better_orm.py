import models
from .DataTypes import *
import sqlite3
import os


class empty:
    pass


class db_settings:
    path = 'database.db'


def for_size(content, request):
    try:
        if content.size:
            request += f'({content.size})'
        return ['ok', request]
    except Exception as ex:
        return ['error', ex]


def for_pk(content, request):
    try:
        if content.primary_key:
            request += f'PRIMARY KEY '
        return ['ok', request]
    except Exception as ex:
        return ['error', ex]


def for_auto_increment(content, request):
    try:
        if content.auto_increment:
            request += f'AUTOINCREMENT '
        return ['ok', request]
    except Exception as ex:
        return ['error', ex]


def for_null(content, request):
    try:
        if not content.nullable:
            request += f'NOT NULL '
        return ['ok', request]
    except Exception as ex:
        return ['error', ex]


def for_unique(content, request):
    try:
        if content.unique:
            request += f'UNIQUE '
        return ['ok', request]
    except Exception as ex:
        return ['error', ex]


def for_default(content, request):
    try:
        if content.default:
            request += f'DEFAULT {content.default}'
        return ['ok', request]
    except Exception as ex:
        return ['error', ex]


def for_check(content, request):
    try:
        if content.check:
            request += f'CHECK {content.check} '
        return ['ok', request]
    except Exception as ex:
        return ['error', ex]


CHECKS = [for_size, for_pk, for_auto_increment,
          for_null, for_unique, for_default, for_check]
a = {}
last_filename = ''


def get_snapshot(table_name, table):
    global a
    for key, value in table.items():
        a[table_name][key] = value.__dict__





def get_table(table_name: str, table: dict):
    returned = f'CREATE TABLE IF NOT EXISTS "{table_name}"('
    global a
    for column, info_column in table.items():
        try:
            if info_column.__class__.__weakref__.__objclass__ == DataType:
                returned += f'"{column}" {info_column.name} '
                a[table_name] = {}
                get_snapshot(table_name, table)
                if info_column.__class__.__name__ == 'ForeignKey':
                    returned += info_column.column + ' '
                else:
                    for check in CHECKS:
                        res = check(info_column, returned)
                        if res[0] == 'ok':
                            returned = res[1]
                returned = returned[:-1]+', '

        except Exception as ex:
            raise Exception(
                "Fuck you ugly motherless. Do you understand that in file models.py you need have only table name as class?")
    if 'PRIMARY KEY' not in returned:
        returned += f'"id" INTEGER PRIMARY KEY  '
    returned = returned[:-2]+')'
    return returned


def create_execute():
    request = ''
    for mod_name, value in models.__dict__.items():
        if hasattr(value, '__module__') and value.__module__ == 'models':
            table_name = mod_name
            mod = dict(value.__dict__)
            for i in empty.__dict__:
                if i in mod:
                    mod.pop(i)
            request += get_table(table_name, mod)+';\n'
    # print(request)
    return request


def create_tables():
    conn = sqlite3.connect(db_settings.path)
    cur = conn.cursor()
    cur.executescript(create_execute() +
                      'CREATE TABLE IF NOT EXISTS "migrations"(filename TEXT)')
    # global last_filename
    # cur.execute(f'INSERT INTO "migrations"(filename) VALUES ({last_filename})')
    conn.commit()


def write_row(table, **qwargs):
    conn = sqlite3.connect(db_settings.path)
    cur = conn.cursor()
    try:
        request = 'INSERT INTO '
        for mod_name, value in models.__dict__.items():
            if table == value:
                request += f'{mod_name}('
                req_val = 'VALUES('
                for k, v in qwargs.items():
                    request += k+', '
                    if v.__class__ == str:
                        req_val += f'\'{v}\','
                    else:
                        req_val += f'{v},'
                request = request[:-2]+') '
                req_val = req_val[:-1]+') '
                request += req_val
                cur.execute(request)
                conn.commit()
                return True
    except Exception as ex:
        raise Exception(
            f'well congratulations your father goes fucking you with a chair on the head with these words: {ex}')


def get_generate_db_script():
    conn = sqlite3.connect(db_settings.path)
    cur = conn.cursor()
    cur.execute('SELECT sql FROM sqlite_master WHERE type="table"')
    old_data = ';\n'.join([x[0] for x in cur.fetchall()])
    new_data = create_execute()
    new_data = new_data.replace('CREATE TABLE IF NOT EXISTS ', '').replace(';', '').replace('\n\n', '\98;0hihihiiiiiiitin')
    old_data = old_data.replace('CREATE TABLE "migrations"(filename TEXT)', '').replace('CREATE TABLE ', '').replace(';', '').replace('\n\n', '\n')

    add_list = []
    remove_list = []
    update_list_r = []
    update_list_a = []

    for new_t in new_data.split('\n'):
        if new_t not in old_data:
            rewrite_i = new_t.split('"')
            if rewrite_i[1] not in old_data:
                add_list.append("CREATE TABLE IF NOT EXIST "+new_t)
            else:
                tables = old_data.split('\n')
                for table in tables:
                    if rewrite_i[1] in table:
                        list_atr = '"'.join(rewrite_i[3:]).split(',')
                        for atr in list_atr:
                            if (atr not in table and atr!=list_atr[-1]) or (atr == list_atr[-1] and atr[:-1] not in table):
                                update_list_a.append(f'ALTER TABLE {rewrite_i[1]} ADD COLUMN {atr[:-1]}')
                        list_atr = table.split("(")[1].split(',')
                        table = '"'.join(rewrite_i[2:])[1:]
                        for atr in list_atr:
                            if ((atr not in table and atr!=list_atr[-1]) or (atr == list_atr[-1] and atr[:-1] not in table)) and "id" not in atr:
                                old_col = atr.split('"')[1]
                                update_list_r.append(f'ALTER TABLE {rewrite_i[1]} DROP COLUMN {old_col};')

    conc = "\n".join(update_list_a)+"\n".join(update_list_r)
    for old_t in old_data.split('\n'):
        if old_t != '':
            edited_table = old_t.split('"')[1]
        if old_t not in new_data and edited_table not in conc:
            rewrite_i = old_t.split('"')
            for i in new_data.split('\n'):
                need_add = True
                i = i.split('"')
                if len(i)>1 and rewrite_i[1] in i[1]:
                    need_add = False
            if need_add:
                remove_list.append(f'DROP TABLE "{rewrite_i[1]}";')


    print('add')
    print(add_list)
    print('-------------------------------------')
    print('update add')
    print(update_list_a)
    print('-------------------------------------')
    print('update remove')
    print(update_list_r)
    print('-------------------------------------')
    print('remove')
    print(remove_list)