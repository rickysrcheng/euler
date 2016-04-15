__author__ = 'TwoZer0Nine'
# Result 26241 returned in 0.272218942642 seconds.

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


def is_prime(n):
    return n in [2, 3, 5] or all(miller_rabin(n, w) for w in [2, 3, 5])

start = time.time()

i = 1
d = 0
result = 0
skip = 0
count = 1

while i <= 100000001 ** 2:  # 1002001
    if (count-1) % 4 == 0:
        if i > 2 and float(d)/float(count) < 0.1:
            result = skip + 1
            break
        skip += 2

    if i > 2 and is_prime(i):
        d += 1

    i += skip

    count += 1

elapsed = time.time() - start

print "Result %s returned in %s seconds." % (result, elapsed)