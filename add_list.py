#Заголовки к заметкам
import datetime
title1 = input("Введите заголовок заметки: ")
content = input("Введите комментарий к заметке: ")
created_date = datetime.datetime.now().date()
print(f"Дата назначения задания: {created_date.strftime("%d.%m")}")
issue_date = input("Введите дату исполнения задания (дд.мм.): ")
title2 = input("Введите заголовок заметки: ")
content = input("Введите комментарий к заметке: ")
created_date = datetime.datetime.now().date()
print(f"Дата назначения задания: {created_date.strftime("%d.%m")}")
issue_date = input("Введите дату исполнения задания (дд.мм.): ")
title3 = input("Введите заголовок заметки: ")
content = input("Введите комментарий к заметке: ")
created_date = datetime.datetime.now().date()
print(f"Дата назначения задания: {created_date.strftime("%d.%m")}")
issue_date = input("Введите дату исполнения задания (дд.мм.): ")
list = [title1,title2,title3]
print(list)