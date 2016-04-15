__author__ = 'TwoZer0Nine'

import time, math, gmpy

start = time.time()
elapsed = 0
lst = [x for x in range(2, 1001) if int(math.sqrt(x) + 0.5)**2 != x]

lst2 = []
for i in xrange(len(lst) - 1, 0, -1):
    curr = lst[i]
    num = 2
    while True:
        e = (num**2 - 1)/curr
        # print num, curr, int(math.sqrt(e))
        if gmpy.is_square(e) and num**2 - curr*e == 1:
            elapsed = time.time() - elapsed - start
            lst2.append(int(num))
            print '%s^2 - %sx%s^2 = 1 in %s' % (num, curr, int(math.sqrt(e)), elapsed)
            break
        num += 1

print max(lst2)