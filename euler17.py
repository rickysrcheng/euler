__author__ = 'TwoZer0Nine'
# result 21124 returned in 0.000720977783203 seconds.

import time

ones = [3, 3, 5, 4, 4, 3, 5, 5, 4]
teens = [6, 6, 8, 8, 7, 7, 9, 8, 8]
tens = [3, 6, 6, 5, 5, 5, 7, 6, 6]

count = 0
start = time.time()
for i in xrange(1, 1000):
    h = i/100
    t = (i / 10) % 10
    o = i % 10
    if h > 0:
        count += ones[h-1] + 7
        if t == 0:
            if o != 0:
                count += ones[o-1] + 3
        elif t == 1:
            if o == 0:
                count += tens[0] + 3
            else:
                count += teens[o-1] + 3
        else:
            if o == 0:
                count += tens[t-1] + 3
            else:
                count += tens[t-1] + ones[o-1] + 3
    else:
        if t == 0:
            if o != 0:
                count += ones[o-1]
        elif t == 1:
            if o == 0:
                count += tens[0]
            else:
                count += teens[o-1]
        else:
            if o == 0:
                count += tens[t-1]
            else:
                count += tens[t-1] + ones[o-1]
count += 3 + 8  # adding the "one thousand"
elapsed = (time.time() - start)

print "result %s returned in %s seconds." % (count, elapsed)