__author__ = 'TwoZer0Nine'
# result 248155780267521 returned in 0.00688505172729 seconds

import time


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

# swapped it around, so instead of looping n
# i'm looping the base and exponent
lst = []
x = 5
while len(lst) != 40:
    a = 2
    while a < 15:
        num = x**a
        if x == digit_sum(num):
            lst.append(x**a)
            # print "%s^%s = %s %s" % (x, a, num, time.time() - start)
        a += 1
    x += 1
lst.sort()
print "result %s returned in %s seconds" % (lst[29], time.time() - start)
