#1)
import datetime
def convert(date_time):
    format = '%b %d %Y %I:%M%p'
    datetime_str = datetime.datetime.strptime(date_time, format)
    return datetime_str
date_time ='Mar 28 2021 03:24PM'
print(convert(date_time))

#------------------------------------------------------------------------------------------------------------------------------------------------------------
#2)

from datetime import date, timedelta
delta = date.today() - timedelta(5)
print('Current Date:',date.today())
print('5 days before Current Date is:',delta)

#---------------------------------------------------------------------------------------------------------------------------------------------------------
#3)
from datetime import datetime
dt =date.today()
print(datetime.combine(dt,datetime.min.time()))

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#4)
import datetime
base = datetime.datetime.today()
for x in range(0,7):
    print(base + datetime.timedelta(days=x))