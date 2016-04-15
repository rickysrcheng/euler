__author__ = 'TwoZer0Nine'


def isPrime(n):
    """Returns True if n is prime"""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

lst = []

for i in xrange(2, 1000001):
    if i not in lst:
        z = str(i)
        a = z[1:] + z[0]
        lst1 = [int(a)]
        while a != z:
            a = a[1:] + a[0]
            lst1.append(int(a))

        flag = True
        for j in lst1:
            if not isPrime(j):
                flag = False
                break
        else:
            for k in lst1:
                lst.append(k)

print len(lst)