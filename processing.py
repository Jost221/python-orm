from better_orm import Better_orm
from models import *

Better_orm.create_tables()
mod = Pizdo.add(name="pukpuk", obub="aooaoaoaoaoa")
mod.save()