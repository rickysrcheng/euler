
# Result 31875000.0 returned in 0.107018947601 seconds

import math, time

start = time.time()
x = 0
y = 0
z = 0
for i in range(0, 500):
    for e in range(0, 500):
        if i + e + math.sqrt(i * i + e * e) == 1000:
            x = i
            y = e
            z = math.sqrt(i ** 2 + e ** 2)

elapsed = time.time() - start
print "Result %s returned in %s seconds" % (x * y * z, elapsed)
