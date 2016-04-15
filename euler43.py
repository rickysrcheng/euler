__author__ = 'TwoZer0Nine'

import itertools, time

start = time.time()

a = list(map(''.join, itertools.permutations("1234567890")))

result = 0

for i in xrange(0, len(a)):
    e = a[i]
    if int(e[1:4]) % 2 == 0 and int(e[2:5]) % 3 == 0 and int(e[3:6]) % 5 == 0 and int(e[4:7]) % 7 == 0 and int(e[5:8]) % 11 == 0 and int(e[6:9]) % 13 == 0 and int(e[7:10]) % 17 == 0:
        result += int(e)

elapsed = time.time() - start

print "result %s returned in %s seconds" % (result, elapsed)