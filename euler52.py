__author__ = 'TwoZer0Nine'

import time

start = time.time()

def is_permutation(x, y):
    lstX = []
    lstY = []

    for i in xrange(len(str(x))):
        lstX.append(x%10)
        x /= 10
    for j in xrange(len(str(y))):
        lstY.append(y%10)
        y /= 10
    lstX.sort()
    lstY.sort()
    if lstX == lstY:
        return True
    return False

i = 1
while True:
    if is_permutation(i, 2*i):
        if is_permutation(i, 3 * i):
            if is_permutation(i, 4 * i):
                if is_permutation(i, 5 * i):
                    if is_permutation(i, 6 * i):
                        break
    i += 1

elapsed = time.time() - start

print "Result %s returned in %s seconds." % (i, elapsed)
