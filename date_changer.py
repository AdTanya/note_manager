import datetime
created_date = datetime.datetime.now()
delta = datetime.timedelta(days=2)
issue_date = created_date + delta
print(created_date.strftime("%d %b"))
print(issue_date.strftime("%d %b"))