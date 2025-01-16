#Заметка
import datetime
title = input("Введите заголовок заметки: ")
content = input("Введите комментарий к заметке: ")
created_date = datetime.datetime.now().date()
print(f"Дата назначения задания: {created_date.strftime("%d.%m")}")
issue_date = input("Введите дату исполнения задания (дд.мм.): ")


