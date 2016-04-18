__author__ = 'TwoZer0Nine'

import time, math, gmpy
import matplotlib.pyplot as plt

# start = time.time()
# elapsed = 0
# lst = [x for x in range(2, 1001) if int(math.sqrt(x) + 0.5)**2 != x]
#
# lst2 = []
# for i in xrange(len(lst) - 1, 0, -1):
#     curr = lst[i]
#     num = 2
#     while True:
#         e = (num**2 - 1)/curr
#         # print num, curr, int(math.sqrt(e))
#         if gmpy.is_square(e) and num**2 - curr*e == 1:
#             elapsed = time.time() - elapsed - start
#             lst2.append(int(num))
#             print '%s^2 - %sx%s^2 = 1 in %s' % (num, curr, int(math.sqrt(e)), elapsed)
#             break
#         num += 1
#
# print max(lst2)

d = 2
x = y = 1
dlst = []
xlst = []
ylst = []
while d < 61:
    if int(math.sqrt(d))**2 == d:
        d += 1
        continue
    else:
        x = 1
        while x**2 - d*(y**2) != 1:
            y = 1
            while x**2 > d*(y**2):
                y += 1
            x += 1
        dlst.append(d)
        xlst.append(x)
        ylst.append(y)
        d += 1

# plt.figure()
# plt.plot(dlst, xlst, 'o')
# plt.xlabel('N')
# plt.ylabel('Max')
# plt.grid(True)
#
# plt.show()

for i in xrange(0, len(xlst)):
    if dlst[i] < xlst[i]:
        print "%s^2 - %s*%s^2 = 1" % (xlst[i], dlst[i], ylst[i])
