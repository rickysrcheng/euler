__author__ = 'TwoZer0Nine'

# Result 171 returned in 0.0088038444519 seconds.

import time

start = time.time()

year = 1901

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_count = 0
week = 1
result = 0
while year < 2001:
    month_count = 0
    while month_count < 12:
        if year % 4 == 0 and month_count == 1:
            for j in xrange(1, month[month_count]+2):
                week %= 7
                week += 1
                if week == 7 and j == 1:
                    result += 1
                    # print month_count + 1, j, year, week
        else:
            for i in xrange(1, month[month_count]+1):
                week %= 7
                week += 1
                if week == 7 and i == 1:
                    result += 1
                    # print month_count + 1, i, year, week
        month_count += 1
    year += 1

elapsed = time.time() - start

print "Result %s returned in %s seconds." % (result, elapsed)