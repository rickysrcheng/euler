__author__ = 'TwoZer0Nine'
# result 40886 returned in 0.0154659748077 seconds


from decimal import *
import math
import time

start = time.time()

def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False


getcontext().prec = 103

res = 0

for i in xrange(2, 100):
    if not is_square(i):
        word = str(Decimal(i).sqrt())

        for e in xrange(0, len(word)-3):
            if word[e].isdigit():
                res += int(word[e])

elapsed = time.time()-start
print "result %s returned in %s seconds" % (res, elapsed)