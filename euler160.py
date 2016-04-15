__author__ = 'TwoZer0Nine'

import math

a = 1
for i in xrange(1, 10000000):
    a *= i % 10 ** 5
    while a % 10 == 0:
        a /= 10
    a %= 100000
print a