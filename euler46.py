__author__ = 'TwoZer0Nine'

# Miller-Rabin: result 5777 returned in 0.541434049606 seconds.
# Sequential search through sieve (1000000): result 5777 returned in 7.39012598991 seconds.
# Reduced sieve (100000): result 5777 returned in 0.651007890701 seconds.

import math
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

a = primes(1000000)


def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False


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

num = 7
flag = True

while flag:
    num += 2
    temp = 0
    if not is_prime_miller_rabin(num):
    #if num not in a:
        for i in a:
            if i < num:
                temp = num - i
                temp /= 2
                if is_square(temp):
                    flag = True
                    #print "%d = %d + 2 x %d^2" % (num, i, temp**0.5)
                    break
            else:
                flag = False

elapsed = time.time() - start
print "result %s returned in %s seconds." % (num, elapsed)
