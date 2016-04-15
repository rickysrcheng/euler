__author__ = 'TwoZer0Nine'
# Result 49 returned in 0.000579118728638 seconds.

import time

# lst = []
# lst2 = []
count = 0

start = time.time()

for i in xrange(1, 10):
    for j in xrange(1, 22):
        if len(str(i**j)) == j:
            count += 1
            print i, j, i**j
            # lst.append(i**j)
            # lst2.append(str(i) + " " + str(j))

elapsed = time.time() - start

print "Result %s returned in %s seconds." % (count, elapsed)