__author__ = 'Gaurav.Khanna'

from datetime import datetime

current_second = datetime.now().second
current_minute = datetime.now().minute
current_hour = datetime.now().hour

current_day = datetime.now().day
current_month = datetime.now().month
current_year = datetime.now().year

print("Current Year :: " , current_year)

if current_year%4==0:
    print("Year is Leap")
else:
    print("Year is not Leap")