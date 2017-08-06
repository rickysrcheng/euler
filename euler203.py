__author__ = 'TwoZer0Nine'

import math
import time

# taken from https://stackoverflow.com/questions/15580291/how-to-efficiently-calculate-a-row-in-pascals-triangle
# calculates a row of Pascal triangle
def pascal(n):
    line = [1]
    for k in range(n):
        line.append(line[k] * (n-k) / (k+1))
    return line


def primes(n):  # sieve of eratosthenes
    ps, sieve = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            ps.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return ps


start = time.time()

pascal_num = []
for i in xrange(1, 51):
    p_row = pascal(i)
    pascal_num = list(set().union(pascal_num, p_row))

pascal_num.sort()

x = int(math.sqrt(pascal_num[-1]))      # x is sqrt(126410606437752), the largest num in the sequence
sieve = primes(x)
prime_power = []
for i in sieve:
    prime_power.append(i**2)

prime_power.sort()

print len(pascal_num), len(prime_power)

new_pascal = []
for i in pascal_num:
    flag = True
    for p in prime_power:
        if p <= i and i % p == 0:
            flag = False
            break
    if flag:
        new_pascal.append(i)

result = sum(new_pascal)

elapsed = time.time() - start
print "Result %s returned in %s seconds." % (result, elapsed)