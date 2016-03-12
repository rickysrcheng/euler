import time
# result 837799 has the collatz value of 525 and is returned in 23.605697155 seconds.


def collatz(n):
    '''
    returns the length of the collatz sequence of n
    '''
    count = 1
    while n != 1:
        if n % 2 == 0:
            count += 1
            n /= 2
        else:
            count += 1
            n = 3*n+1
    return count


n = 1
best = 0
bestC = 0
start = time.time()
while n <= 1000000:
    a = collatz(n)
    if a > bestC:
        best = n
        bestC = a
    n += 1
elapsed = time.time()-start
print "result %s has the collatz value of %s and is returned in %s seconds." % (best, bestC, elapsed)