import math
import time

# result 142913828922 returned in 11.8557579517 seconds. Using the first isPrime
# result 142913828922 returned in 11.1330280304 seconds. Using the second isPrime


def isPrime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

# def isPrime(n):
#     """Returns True if n is prime"""
#     if n == 2:
#         return True
#     if n == 3:
#         return True
#     if n % 2 == 0:
#         return False
#     if n % 3 == 0:
#         return False
#     i = 5
#     w = 2
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         i += w
#         w = 6 - w
#
#     return True

start = time.time()  
res = 0
for i in range(2, 2000001):
    if isPrime(i):
        res += i
elapsed = (time.time() - start)
 
print "result %s returned in %s seconds." % (res, elapsed)
