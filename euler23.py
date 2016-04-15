__author__ = 'TwoZer0Nine'
import math, time
# result 4179871 returned in 8.96733498573 seconds


def factors(n):
    return list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(math.sqrt(i)) + 1) if n % i == 0))))

start = time.time()

lst = []
lst2 = []

for i in xrange(1, 28124):
    x = factors(i)
    x.remove(i)
    if sum(x) > i:
        lst.append(i)

for i in xrange(0, len(lst)):
    for j in xrange(i, len(lst)):
        n = lst[i] + lst[j]
        if n < 28124:
            lst2.append(n)
        else:
            break

lst2.sort()
lst2 = list(set(lst2))
result = 0
for e in xrange(0, 24):
    result += e

for i in xrange(0, len(lst2) - 1):
    if lst2[i] < 28123:
        for j in xrange(lst2[i]+1, lst2[i+1]):
            result += j

elapsed = time.time() - start
print "result %s returned in %s seconds" % (result, elapsed)



