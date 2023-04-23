from better_orm import Better_orm
from models import *

Better_orm.get_generate_db_script()

# Better_orm.create_tables()
# Better_orm.write_row(a, var1='strokaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
# b = a
# b.var1 = 'ababababababbaa'
# b.save()
# b = a.read()
# for i in b:
#     print(i.var1)

# Better_orm.write_row(
#     User,
#     name = "OLEG",
#     age = 5,
#     dick_lenght = 20
# )