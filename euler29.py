__author__ = 'TwoZer0Nine'

lst = []

for i in xrange(2, 101):
    for j in xrange(2, 101):
        a = i**j
        if a not in lst:
            lst.append(a)

print len(lst)
