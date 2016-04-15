__author__ = 'TwoZer0Nine'
# result 8581146 returned in 76.388710022 seconds.

import time

count = 0
dct = {}
start = time.time()

for i in xrange(2, 10000001):

    a = str(i)
    helperLst = [a]
    z = 0

    while True:
        z = 0
        for letters in a:
            z += int(letters) ** 2
        a = str(z)
        if a in dct:
            if dct[a] == "yes":
                dct[str(i)] = "yes"
            else:
                dct[str(i)] = "no"
            break
        elif a == "89":
            dct[str(i)] = "yes"
            break
        elif a == "1":
            dct[str(i)] = "no"
            break

for j in dct:
    if dct.get(j) == "yes":
        count += 1

elapsed = (time.time() - start)

print "result %s returned in %s seconds." % (count, elapsed)