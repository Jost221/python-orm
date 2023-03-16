# python-orm-custom 

История такова:

> Писал я значит проект и меня так сильно затрахала привязанность 
либо к одному фреймворку либо отсутствие миграций как например в 
SQLAlhimy (либо я просто не разобрался как они работают) что решил 
ебануть свою orm минут за 30 я понял что это относительно не сложно 
и начал хуярить

## How to use?

Now i'm testing this code not as library, but as live work file.
Consider how to use

---

### Create DB

you need create file
> models.py

example of a filling file

```Python
import DataTypes

class a:
    var1 = DataTypes.String(default='default', size=10)
    var2 = DataTypes.Integer(primary_key=True, auto_increment=True) 

class abob:
    name = DataTypes.String(primary_key=True)`
```

then you need run function `create_db()`

---

if you need custom name db you need add in envirements parametr DATABASE_NAME

value db name take vrom envirements with help `os` library

you can add in your code this line

```python
import os

os.environ['DATABASE_NAME'] = 'db_name.db'
```
---

`create_db_from_models.py` creates your database. With this data you get next data base:

| a | aboba |
|-----:|-----------|
|var1|name|
|var2| |

---

## Write data

For write data with this library you need using function `write_db(table_name, **data)`

Example:
```python
write_db(models.a, var1='value1')
```

with this function your database get next value
Table a:

| var1 | var2 |
|-----:|-----------|
|"value1"|1|

---

after write data you need and read it. for read usin function `read_db(models)`

Exemple:
```python
result = read_db(models.a)
```
in result you get list object 'a' with variables var1 and var2

<picture>
  <img alt="Shows an illustrated sun in light mode and a moon with stars in dark mode." src="https://im.wampi.ru/2023/03/10/image1cf39d530b24f1ae.png">
</picture>

8========0

further more.
stages of development:
1. adding complex values such as datetime
2. Validations for programmer errors when creating a database
3. Adding migration capability
4. Injection protection