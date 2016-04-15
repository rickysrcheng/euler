__author__ = 'TwoZer0Nine'
# Result 972 returned in 0.681791067123 seconds.

import time

start = time.time()
maximum = 0
ii = 0
jj = 0
for i in xrange(99, 2, -1):
    for j in xrange(99, 2, -1):
        a = pow(i, j)
        result = 0
        while a > 0:
            result += a % 10
            a /= 10
        if result > maximum:
            maximum = result
            ii = i
            jj = j

elapsed = time.time() - start

print "Result %s returned in %s seconds." % (maximum, elapsed)