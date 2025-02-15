from datetime import datetime,timedelta
today =datetime.today()
newdate =today.replace(microsecond=0)
print(newdate)