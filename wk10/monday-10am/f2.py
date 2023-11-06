import datetime

dt = datetime.date(2020, 3, 21)
print(dt)
print(dt.year, dt.month, dt.day)
print(dt.strftime("%B"))  # March

rnd = datetime.date.today()
print(rnd)

dtt = datetime.datetime(2020, 3, 21, 15, 45)
print(dtt)

dttrn = datetime.datetime.now()
print(dttrn)
