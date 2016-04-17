__author__ = 'TwoZer0Nine'
# result -59231 returned in 2.73620605469 seconds

import time


def miller_rabin(n, witness): # false if composite
    # print "Miller-Rabin"
    if n % witness == 0: return False
    m = n - 1
    b = 0
    while m % 2 == 0:
        m /= 2
        b += 1
    w = pow(witness, m, n)
    if w == 1: return True
    for _ in range(b):
        if w == n - 1: return True
        w = pow(w, 2, n)
        if w == 1: return False
    return False


def is_prime_miller_rabin(n):
    return n in [2, 3, 5] or all(miller_rabin(n, w) for w in [2, 3, 5])

def primes(n): # sieve of eratosthenes
    ps, sieve = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            ps.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return ps

start = time.time()

a = -999
p = primes(1000)
maximum = 0
result = 0

while a <= 1000:
    for b in p:
        n = 0
        num = b
        #print num, a, b
        #print a, b
        while num > 1 and is_prime_miller_rabin(num):
            #print a, b, n, num
            n += 1
            num = (n ** 2) + (a * n) + b
        if n > maximum:
            maximum = n
            result = a*b
    a += 1

print "result %s returned in %s seconds" % (result, time.time() - start)