__author__ = 'TwoZer0Nine'
# Result 871198282 returned in 0.00997400283813 seconds.

import time

start = time.time()

with open("/Users/Ricky/Desktop/Python/p022_names.txt", "r") as names:
    words = names.read().translate(None, '"').split(',')
names.close()
words.sort()
total = 0
count = 1


for i in words:
    value = 0
    for l in i:
        value += ord(l) - 64
    total += value * count
    count += 1

elapsed = time.time() - start

print "Result %s returned in %s seconds." % (total, elapsed)
