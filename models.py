from better_orm import DataTypes
# play write использовать для парса леруа
class a(DataTypes.Table_Engine):
    var1 = DataTypes.String(default='default', size=10)
    var2 = DataTypes.Integer(primary_key=True)
    var3 = DataTypes.String(default='default', size=8)

class tak(DataTypes.Table_Engine):
    data = DataTypes.String()
    paba = DataTypes.Integer(primary_key=True)

class abob(DataTypes.Table_Engine):
    name = DataTypes.String(primary_key=True)
    surname = DataTypes.String()
    # patronomic = DataTypes.String()

class Pizdos(DataTypes.Table_Engine):
    obub = DataTypes.String()

class Pizdo(DataTypes.Table_Engine):
    name = DataTypes.String(primary_key=True)
    obub = DataTypes.String()

# class huyak(DataTypes.Table_Engine):
#     puuuuk = DataTypes.String()

class Todos(DataTypes.Table_Engine):
    fk = DataTypes.ForeignKey('Pizdos.obub')

class User(DataTypes.Table_Engine):
    name = DataTypes.String()
    age = DataTypes.Integer()
    dick_lenght = DataTypes.Integer()

class User1(DataTypes.Table_Engine):
    pakpab = DataTypes.Integer()

class User2(DataTypes.Table_Engine):
    pakpab = DataTypes.Integer()

class User3(DataTypes.Table_Engine):
    pakpab = DataTypes.Integer()