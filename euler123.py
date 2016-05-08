__author__ = 'TwoZer0Nine'
# result 21035 returned in 73.235658884 seconds

import time

def primes(n): # sieve of eratosthenes
    ps, sieve = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            ps.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return ps

start = time.time()
lst = primes(1000000)
print len(lst)

for n in xrange(0, len(lst)):
    p = lst[n]
    r = ((p+1)*(n+1) + (p-1)**(n+1)) % (p**2)
    if r > 10**10:
        print n, p, r
        break

print "result %s returned in %s seconds" % (n+1, time.time()-start)