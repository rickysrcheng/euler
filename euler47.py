__author__ = 'TwoZer0Nine'

import time

count = 0

start = time.time()


def factorization(n):
    lst = []
    for d in [2, 3]:
        if n % d == 0:
            lst.append(d)
            while n % d == 0:
                n /= d
    f = 5
    step = 2
    while True:
        if n == 1:
            return lst

        if n < f ** 2:
            lst.append(n)
            return lst

        r = n % f

        if r > 0:
            f += step
            step = 6 - step
        elif r == 0:
            if f not in lst:
                lst.append(f)
            n /= f

t = 646
while True:
    a = factorization(t)
    if count == 4:
        break

    if len(a) == 4:
        count += 1
    else:
        count = 0
    t += 1

elapsed = time.time() - start

print "Result %s returned in %s seconds" % (t - 4, elapsed)