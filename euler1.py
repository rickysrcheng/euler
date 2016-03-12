__author__ = 'TwoZer0Nine'
# Result 233168 returned in 0.000244855880737 seconds.

import time

start = time.time()
result = 0

for i in xrange(1000):
    if i % 3 == 0 or i % 5 == 0:
        result += i

elapsed = time.time() - start
print "Result %s returned in %s seconds." % (result, elapsed)