__author__ = 'TwoZer0Nine'
# Result 249 returned in 0.109929084778 seconds.

import time

start = time.time()

result = 0
lst = []

for i in xrange(10, 10001):
    a = i + int(str(i)[::-1])
    count = 1
    while str(a) != str(a)[::-1] and count <= 50:
        a += int(str(a)[::-1])
        count += 1
    if count >= 50:
        lst.append(i)
        result += 1

elapsed = time.time() - start

print "Result %s returned in %s seconds." % (result, elapsed)
for e in lst:
    if str(e) == str(e)[::-1]:
        print e