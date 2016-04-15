__author__ = 'TwoZer0Nine'
# n is less than 85 for n ** 4
# n is less than 369 for n ** 3
# n is less than 7071 for n ** 2


def primes(n): # sieve of eratosthenes
    ps, sieve = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            ps.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return ps

count = 0
lst = []
A = primes(7100)
for i in xrange(0, len(A)):
    A[i] *= A[i]

B = primes(380)
for i in xrange(0, len(B)):
    B[i] = pow(B[i], 3)

C = primes(89)
for i in xrange(0, len(C)):
    C[i] = pow(C[i], 4)

t = 1000#50000000
n = 0

for c in C:
    for b in B:
        for a in A:
            n = a + b + c
            if n in lst:
                if count < 100:
                    print "A", a, b, c, n
                pass
            elif a < t and b < t and c < t and n < t:
                lst.append(n)
                count += 1
                #if count < 100:
                 #   print count, a, b, c, n
print count

# for i in A:
#     a = pow(i, 2)
#     for j in B:
#         b = pow(j, 3)
#         for k in C:
#             c = pow(k, 4)
#             temp = a + b + c
#             if temp < 50000000 and temp not in lst:
#                 lst.append(temp)
#
#print len(lst)

