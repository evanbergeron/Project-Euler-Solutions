import datetime
result = 0
for year in xrange(1901, 2001):
    for month in xrange(1, 13):
        thatDay = datetime.datetime(year, month, 1)
        if thatDay.weekday() == 0: result += 1

print result
