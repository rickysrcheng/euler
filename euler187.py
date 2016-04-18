__author__ = 'TwoZer0Nine'
# result 17427258 returned in 29.3015041351 seconds

import time, math


def primes(n): # sieve of eratosthenes
    ps, sieve = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            ps.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return ps


n = 10**8
start = time.time()
lst = primes(n/2)
s = len(lst)
count = 0
for i in xrange(0, s):
    for j in xrange(i, s):
        if lst[i]*lst[j] < n:
            count += 1
        else:
            break

print "result %s returned in %s seconds" % (count, time.time()-start)
