__author__ = 'TwoZer0Nine'
# Result 7652413 returned in 114.748403072 seconds.

import time


def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in xrange(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

start = time.time()

Max = 0
for i in xrange(7654321):
    if is_prime(i):
        a = str(i)
        lst = []
        if "0" not in a:
            for j in range(len(a)):
                lst.append(0)
            for s in a:
                if int(s) > len(a):
                    break
                else:
                    lst[int(s)-1] += 1
            for e in lst:
                if e > 1 or e == 0:
                    break
            else:
                if i > Max:
                    Max = i


elapsed = time.time() - start

print "Result %s returned in %s seconds." % (Max, elapsed)