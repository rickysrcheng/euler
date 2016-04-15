__author__ = 'TwoZer0Nine'

import math

result = 0

for i in xrange(3, 99999):
    z = i
    num = 0
    while z > 0:
        num += math.factorial(z % 10)
        z /= 10
    if num == i:
        print i
        result += i

print result