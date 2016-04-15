__author__ = 'TwoZer0Nine'

import math, time


def is_triangular(n):
    x = int((math.sqrt(1 + 8 * n) - 1) / 2)

    return (x * (x + 1)) / 2 == n


def is_pentagonal(n):
    x = int((math.sqrt(1 + 24 * n) + 1) / 6)

    return (x * (3 * x - 1)) / 2 == n


def is_hexagonal(n):
    x = int((math.sqrt(1 + 8 * n) + 1) / 4)

    return (x * (2 * x - 1)) == n

lst = []
result = 0
start = time.time()

for i in xrange(144, 100000):
    lst.append(i * (2 * i - 1))

for e in lst:
    if is_triangular(e) and is_pentagonal(e):
        result = e
        break

elapsed = time.time() - start

print "Result %s returned in %s seconds." % (result, elapsed)