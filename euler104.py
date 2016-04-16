__author__ = 'TwoZer0Nine'
# result 329468 returned in 24.9182720184 seconds

import time


def is_pandigital(s):
    lst = [str(x) for x in range(1, 10)]
    if set(lst) == set(list(s)):
        return True
    else:
        return False

start = time.time()
lst = [str(x) for x in range(1, 10)]
lst = set(lst)
a = 1
b = 1
ctr = 1
while True:
    if lst == set(list(str(a % 1000000000))):
        if lst == set(list(str(a)[0:9])):
            break
    a, b = b, a+b
    ctr += 1
print "result %s returned in %s seconds" % (ctr, time.time()-start)
