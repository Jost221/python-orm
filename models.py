from better_orm import DataTypes

class a(DataTypes.Table_Engine):
    var1 = DataTypes.String(default='default', size=10)
    var2 = DataTypes.Integer(primary_key=True) 

class abob(DataTypes.Table_Engine):
    name = DataTypes.String(primary_key=True)

class Pizdos(DataTypes.Table_Engine):
    obub = DataTypes.String()

class Pizdo(DataTypes.Table_Engine):
    name = DataTypes.String(primary_key=True)
    obub = DataTypes.String()

class Todos(DataTypes.Table_Engine):
    fk = DataTypes.ForeignKey(Pizdos.obub)