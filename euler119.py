__author__ = 'TwoZer0Nine'
# result 248155780267521 returned in 0.0361828804016 seconds

import time

def increment(lst):
    lst[0] += 1
    for i in xrange(0, len(lst)):
        if lst[i] == 10:
            lst[i] = 0
            if i == len(lst) - 1:
                lst.append(1)
            else:
                lst[i+1] += 1
        else:
            return lst
    return lst


def make_list(n):
    lst = []
    while n >= 10:
        lst.append(n % 10)
        n /= 10
    lst.append(n)
    return lst

def digit_sum(n):
    digit_sum = 0
    while n > 0:
        digit_sum += n%10
        n /= 10
    return digit_sum

start = time.time()

# brute force method
# got to '46^5 = 205962976, a16' in 457 seconds (7:37)
# a17 is due next in 18 min
#
# num = 2
# lst = [2]
# rlst = []
# while len(rlst) != 30:
#     x = sum(lst)
#     a = 2
#     while x != 1 and x**a <= num:
#         if x**a == num:
#             rlst.append(num)
#             print "%s^%s = %s %s" % (x, a, num, time.time() - start)
#             num = (x+1)**a - 1
#             lst = make_list(num)
#             break
#         a += 1
#     num += 1
#     lst = increment(lst)

lst = []
x = 5
while len(lst) != 40:
    a = 2
    while a < 15:
        num = x**a
        #print x, a, num, digit_sum(num)
        if x == digit_sum(num):
            lst.append(x**a)
            print "%s^%s = %s %s" % (x, a, num, time.time() - start)
        a += 1
    x += 1
lst.sort()
print lst
print "result %s returned in %s seconds" % (lst[29], time.time() - start)
