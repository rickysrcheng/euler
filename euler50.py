__author__ = 'TwoZer0Nine'


def primes(n): # sieve of eratosthenes
    ps, sieve = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            ps.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return ps


def isPrime(n):
    """Returns True if n is prime"""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w

    return True

a = primes(4000)

b = 0

for i in range(len(a)):
    b += a[i]
    if b > 1000000:
        b -= a[i]
        break

for j in range(len(a)):
    b -= a[j]
    if isPrime(b):
        break

print b