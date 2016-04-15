__author__ = 'TwoZer0Nine'

# Result 402 returned in 80.5682361126 seconds.

import math
import time

start = time.time()

count = 0

for i in xrange(2, 1000000):
    z = i
    temp = [i]
    while True:
        b = z
        c = 0
        while b > 0:
            c += math.factorial((b % 10))
            b /= 10
        if c in temp:
            if len(temp) == 60:
                print i
                count += 1
            break
        else:
            temp.append(c)
            z = c

elapsed = time.time() - start

print "Result %s returned in %s seconds." % (count, elapsed)