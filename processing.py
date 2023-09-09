from bs_orm import Requests
import models 
import datetime

Requests.db_settings.models = models
# Requests.db_settings.path = './baza/database.db' поправить
Requests.migrate()

# for i in models.Chat.search(Id=757577290):
#     i.update(Group = 'buba', PinnedMessageId = 1211, Time = '11:51')

# models.Chat.add(Time=datetime.datetime.now())
# models.Chat.add(Time=datetime.datetime.now())

records = models.Chat.search()
print(records[0].Id)
# records = models.Chat.search()
# Requests.update(records, Time=datetime.datetime.now())
# for i in records:
    # print(i.__dict__)
# pass



# Better_orm.write_row(
#     User,
#     name = "OLEG",
#     age = 5,
#     dick_lenght = 20
# )