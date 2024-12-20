# Solution to programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar

# This function counts the number of the given weekday for the
# specified year and month and returns the result
def countdays(theyear, themonth, whichday):
    daycount = 0
    weekslist = calendar.monthcalendar(theyear, themonth)
    for week in weekslist:
        if week[whichday] != 0:
            daycount += 1
    return daycount


year = 2024
month = 12
day = 0
result = countdays(year, month, day)

