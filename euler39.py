__author__ = 'TwoZer0Nine'
# result 840 returned in 56.7725179195 seconds
# runs in O(n^3) time. there's gotta be a more efficient way

import math, time


def max_perimeter(n):
    lst = []
    lst2 = []
    for i in xrange(1, n/2):
        for j in xrange(1, n/2):
            h = int(math.sqrt(i**2+j**2))
            s = i**2 + j**2
            if h**2 == s:
                if i + j + h == n:
                    lst.append(i)
                    lst.append(j)
                    lst.append(h)
                    lst.sort()
            if len(lst) == 3:
                if lst not in lst2:
                    lst2.append(lst)
                lst = []
    return lst2


start = time.time()
maximum = 0
result = 0
print max_perimeter(840)
# for j in xrange(3, 1001):
#     n = max_perimeter(j)
# #    print j, n, max_perimeter(j)
#     if n > maximum:
#         maximum = n
#         result = j

print "result %s returned in %s seconds" % (result, time.time() - start)

