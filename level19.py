from datetime import date
from datetime import timedelta as td

start = date(1901, 1, 1)
end = date(2000, 12, 31)
day = start


def diff_months(a, b):
    return (b.year - a.year) * 12 + b.month - a.month

monthcount = diff_months(start, end)
# print start.month
# print monthcount
counter = 0
for i in range(1, monthcount + 1):
    i = i % 12
    if i == 0:
        i = 12
    day = date(day.year, i, 1)
    # print day
    if day.weekday() == 6:  # check whether sunday
        counter += 1
    if i == 12:
        newYear = day.year + 1
        day = date(newYear, 1, 1)


print counter
