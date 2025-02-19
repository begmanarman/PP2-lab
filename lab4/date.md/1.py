from datetime import datetime,timedelta
today = datetime.today()
newdate = today - timedelta(days=5)
print(newdate.strftime("%d-%m-%Y"))