__author__ = 'TwoZer0Nine'
# result 2906969179 returned in 0.999319076538 seconds

import math, time


def is_palindrome(n):
    s = str(n)
    s1 = list(s[:len(s)/2])
    s2 = list(reversed(s[len(s)/2:])) if len(s) % 2 == 0 else list(reversed(s[len(s)/2 + 1:]))
    return s1 == s2

lst = [x**2 for x in xrange(1, int(math.sqrt(10**8))+1)]
# print len(lst)
start = time.time()
dupes = []
result = 0
# count = 0


for i in xrange(0, len(lst)):
    # rslt = []
    rolling_sum = lst[i]
    # rslt.append(int(math.sqrt(lst[i])))
    for j in xrange(i + 1, len(lst)):
        rolling_sum += lst[j]
        # rslt.append(int(math.sqrt(lst[j])))
        if rolling_sum >= 10**8:
            break
        elif is_palindrome(rolling_sum) and rolling_sum not in dupes:
            # print rolling_sum
            dupes.append(rolling_sum)
            result += rolling_sum
            # count += 1
# print count
print "result %s returned in %s seconds" % (result, time.time()-start)
