__author__ = 'TwoZer0Nine'
# Result 173 returned in 0.00318598747253 seconds.

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


start = time.time()

result = 0
i = 2
while True:
    prime = 3*i*(i-1)+1
    if prime > 10**6:
        break
    if is_prime_miller_rabin(prime):
        result += 1
    i += 1


elapsed = time.time() - start
print "Result %s returned in %s seconds." % (result, elapsed)
