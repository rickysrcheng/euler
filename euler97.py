__author__ = 'TwoZer0Nine'
# Result 8739992577 return in 0.117249011993 seconds.

import time

start = time.time()

# result = pow(28433 * pow(2, 7830457) + 1, 1, 10**10)
result = (28433 * 2 ** 7830457 + 1) % 10 ** 10
elapsed = time.time() - start

print "Result %s return in %s seconds." % (result, elapsed)