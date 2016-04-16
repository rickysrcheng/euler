__author__ = 'TwoZer0Nine'
# result 333082500 returned in 0.000331878662109 seconds

import time
# import matplotlib.pyplot as plt
#
# x = []
# y = []
#
# for num in range(3, 21):
#     n = num**2
#     maximum = 0
#     if num < 21:
#         compare = 0.5
#     elif num < 50:
#         compare = 0.9
#     elif num < 120:
#         compare = 0.96
#     else:
#         compare = 0.98
#     while n > float(num**2)*compare:
#         c = ((num - 1)**n + (num + 1)**n) % (num**2)
#         if c > maximum:
#             maximum = c
#         n -= 1
#     x.append(num)
#     y.append(float(maximum)/float(num**2))
#
# plt.plot(x, y)
# plt.xlabel('Number')
# plt.ylabel('Ratio')
# plt.grid(True)
# plt.show()
#

start = time.time()
# for i in xrange(3, 101):
#     maximum = i*(i-2) if i % 2 == 0 else i*(i-1)
#     result += maximum
#     x.append(i)
#     y.append(float(maximum)/float(i**2))


# one liner
result = sum([i * (i-2) if i % 2 == 0 else i * (i-1) for i in xrange(3, 1001)])

print "result %s returned in %s seconds" % (result, time.time()-start)

# plt.plot(x, y)
# plt.xlabel('Number')
# plt.ylabel('Ratio')
# plt.grid(True)
# plt.show()