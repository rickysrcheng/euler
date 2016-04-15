__author__ = 'TwoZer0Nine'

import time

start = time.time()


def primes(n): # sieve of eratosthenes
    ps, sieve = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            ps.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return ps


def right_side(n):
    t = n/10
    flag = True
    while t > 0:
        if t in a:
            flag = True
        else:
            flag = False
            break
        t /= 10
    return flag


def left_side(n):
    modder = 10 ** (len(str(n))-1)
    t = n % modder
    flag = True
    while t > 0:
        if t in a:
            flag = True
        else:
            flag = False
            break
        modder = 10 ** (len(str(t))-1)
        t %= modder
    return flag


a = primes(1000000)
lst = []

for e in a:
    if len(str(e)) > 1 and right_side(e) and left_side(e):
        print e, time.time()-start
        lst.append(e)

elapsed = time.time() - start

print lst

print "Result %s returned in %s seconds" % (sum(lst), elapsed)