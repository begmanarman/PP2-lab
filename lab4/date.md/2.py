from datetime import datetime,timedelta
today =datetime.today()
yes = today-timedelta(days=1)
tom = today + timedelta(days=1)
print(today.strftime("%d"))
print(yes.strftime("%d"))
print(tom.strftime("%d"))