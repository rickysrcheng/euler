__author__ = 'TwoZer0Nine'
# Result 162 returned in 0.0134711265564 seconds

import time


start = time.time()


tri_num = [n*(n+1)/2 for n in range(1, 20)]

tri = open("/Users/Ricky/Desktop/Python/p042_words.txt", "r")

alphabet = "_ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lst = []
word = ""
count = 0
value = 0

while True:
    rd = tri.read(1)

    if rd == ".":
        break
    elif rd in alphabet:
        value += alphabet.index(rd)
    else:
        if value in tri_num:
            count += 1
        value = 0

tri.close()

elapsed = time.time() - start

print "Result %s returned in %s seconds" % (count, elapsed)