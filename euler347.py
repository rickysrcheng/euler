__author__ = 'TwoZer0Nine'
# result 11109800204052 returned in 7.87170004845 seconds

import math, time


def primes(n): # sieve of eratosthenes
    ps, sieve = [], [True] * (n + 1)
    for i in range(2, n + 1):
        if sieve[i]:
            ps.append(i)
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return ps


def factor(p, q, s):
    pe = 1
    maximum = 0
    ps = 0
    while ps * q <= s:
        ps = p**pe
        qe = 1
        qs = q**qe
        while ps * qs <= s:
            qe += 1
            qs = q**qe
        qs /= q
        if s >= qs * ps > maximum:
            maximum = qs * ps
        pe += 1
    return maximum


start = time.time()
s = 10000000
lst = primes(s)
result = 0
for i in xrange(0, len(lst)):
    p = lst[i]
    for j in xrange(i + 1, len(lst)):
        q = lst[j]
        if p * q > s:
            break
        result += factor(p, q, s)

        # if p == 2 and q == 5:
        #     mp = s
        #     mq = 0
        # else:
        #     pe = int(math.log(float(s)/float(q), p))
        #     qe = int(math.log(float(s)/float(p), q))
        #     mp = p ** pe * q if pe > 0 else 0
        #     mq = q ** qe * p if qe > 0 else 0
        # if mp > mq:
        #     print "%s^%s * %s = %s" % (p, pe, q, mp)
        #     result += mp
        # else:
        #     print "%s^%s * %s = %s" % (q, qe, p, mq)
        #     result += mq

print "result %s returned in %s seconds" % (result, time.time() - start)
