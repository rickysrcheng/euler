__author__ = 'TwoZer0Nine'
# Result 443839 returned in 6.85296702385 seconds.

import time

result = 0
start = time.time()
for i in xrange(1000, 1000000):
    a = i
    temp = 0
    while a > 0:
        temp += pow(a % 10, 5)
        a /= 10
    if temp == i:
        result += i

elapsed = time.time() - start
print "Result %s returned in %s seconds." % (result, elapsed)