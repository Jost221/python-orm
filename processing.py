from bs_orm import Requests
import models 

# Requests.db_settings.models = models
Requests.create_tables(models)

# Better_orm.create_tables()


# for i in models.Chat.search(Id=757577290):
#     i.update(Group = 'buba', PinnedMessageId = 1211, Time = '11:51')

models.Chat.update(
    models.Chat.search(
        Id=757577290
    ),
    Group=None
)


# Better_orm.write_row(
#     User,
#     name = "OLEG",
#     age = 5,
#     dick_lenght = 20
# )