__author__ = 'TwoZer0Nine'

a = 1
b = 1
index = 2
c = 0

while c < 1000:

    a, b = b, b + a
    c = len(str(b))
    index += 1

print index, c

