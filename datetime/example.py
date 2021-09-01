import datetime

print(datetime.datetime.now())
now = datetime.datetime.now()
yesterday = datetime.datetime(2021,2,11,0,0,0)
delta = now - yesterday
print(delta.days)
thousanddays = datetime.timedelta(1000)
print(now+thousanddays)
print(now.strftime("%d/%m/%Y - %H:%M"))