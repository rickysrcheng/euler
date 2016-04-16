__author__ = 'TwoZer0Nine'
import time


def bouncy(n):
    lst = []
    inc = False
    dec = True
    while n >= 10:
        lst.append(n % 10)
        n /= 10
    lst.append(n)
    if lst[0] < lst[len(lst)-1]:
        dec = True
    else:
        inc = True

    for i in xrange(0, len(lst)-1):
        if inc:
            if lst[i] >= lst[i+1]:
                continue
            else:
                return True
        elif dec:
            if lst[i] <= lst[i+1]:
                continue
            else:
                return True
    return False

start = time.time()

n = 99.0
b = 0.0
ratio = b / (n + b)
num = 99
while ratio < 0.99:
    num += 1
    if bouncy(num):
        b += 1
    else:
        n += 1
    ratio = b / (n + b)

elapsed = time.time() - start
print "result %s returned in %s seconds" % (num, elapsed)


