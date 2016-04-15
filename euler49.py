__author__ = 'TwoZer0Nine'

import itertools


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


a = []
temp = []
step = 0
results = []
for i in xrange(1001, 10000):
    if is_prime_miller_rabin(i):
        a.append(i)


for j in a:
    b = list(map("".join, itertools.permutations(str(j))))
    for k in b:
        if k[0] != "0" and is_prime_miller_rabin(int(k)):
            temp.append(k)

    for m in temp:
        for n in temp:
            if m != n:
                step = int(n) - int(m)
                for x in temp:
                    if x != m and x != n and int(x) - int(n) == step and x not in results:
                        print m, n, x, step
                        results.append(x)
                        results.append(n)
                        results.append(m)
                        break
        step = 0
    temp = []


print results
