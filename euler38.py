__author__ = 'TwoZer0Nine'

import time

start = time.time()


def is_pandigital(n):
    a = "123456789"
    for i in a:
        if i not in n:
            return False
    return True

a = 1
maximum = 0

while a < 10000:
    string = ""

    i = 1
    while len(string) < 9:
        string += str(a * i)
        i += 1
    if len(string) == 9 and is_pandigital(string):
        if int(string) > maximum:
            maximum = int(string)
    a += 1

elapsed = time.time() - start
print "Result %s returned in %s seconds." % (maximum, elapsed)