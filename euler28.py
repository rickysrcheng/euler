__author__ = 'TwoZer0Nine'
# Result 669171001 returned in 0.000670909881592 seconds.

import time

start = time.time()

i = 1
Sum = 0
skip = 0
count = 0
while i <= 1001 ** 2:  # 1002001
    if count % 4 == 0:
        skip += 2
    Sum += i
    i += skip

    count += 1

elapsed = time.time() - start

print "Result %s returned in %s seconds." % (Sum, elapsed)