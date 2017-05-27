__author__ = 'TwoZer0Nine'

from math import log, sqrt
import time


"""
Converts int n to base b
Correct up to base 10 since no symbols other than numeral symbols are utilised
"""
def int2base(n, b):
    result = ""
    power = int(log(n, b))
    for i in xrange(power, -1, -1):
        if n - b**i >= 0:
            tmp = n/(b**i)
            result += str(tmp)
            n -= tmp * b**i
        elif i == 0:
            result += str(n)
        else:
            result += "0"
        #print result, n, b**i

    return result


def base2int(n, b):
    length = len(n)
    result = 0
    for i in xrange(0, length):
        result += b**i
    return result


start = time.time()

m = 10**12

lst = set()
confirmed = set([1])
result = 1
tmp = len(int2base(m, 2))

for i in xrange(3, tmp + 1):
    s = "1"*i
    for j in xrange(2, int(sqrt(m))):
        num = int(base2int(s, j))
        if num < m:
            c = num in confirmed
            l = num in lst
            if not l:
                lst.add(num)
            elif not c:
                confirmed.add(num)
                result += num
        else:
            break

# print len(lst)

for i in lst:
    if base2int("11", i - 1) == i:
        c = i in confirmed
        if not c:
            confirmed.add(num)
            result += i

elapsed = time.time() - start
print "Result %s returned in %s seconds." % (result, elapsed)



