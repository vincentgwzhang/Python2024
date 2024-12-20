import calendar
import datetime

def count_days(year, month, whichday):
    date = datetime.date(year, month, 1)
    weekday_index = date.weekday()

    return 0

testyear = 2024
testmonth = 12
testday = 0
result = count_days(testyear, testmonth, testday)