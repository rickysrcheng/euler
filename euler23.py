__author__ = 'TwoZer0Nine'
# result 4179871 returned in 9.68146109581 seconds

import math, time

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
        #print lst.index(i) + 1, i, sum(x)

for i in xrange(0, len(lst)):
    for j in xrange(i, len(lst)):
        n = lst[i] + lst[j]
        if n < 30000:
            #print lst[i], lst[j], n
            lst2.append(n)
        else:
            break

lst2.sort()
lst2 = list(set(lst2))
result = 0

for i in xrange(0, len(lst2) - 1):
    if i == 0:
        for e in xrange(0, lst2[i]):
            result += e
    if lst2[i] < 28123:
        for e in xrange(lst2[i]+1, lst2[i+1]):
            #if e < 1000:
            #    print e
            result += e

elapsed = time.time() - start
print "result %s returned in %s seconds" % (result, elapsed)



