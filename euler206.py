# result 1389019170 returned in 9.88262605667 seconds
import time

start = time.time()
n = 101010101
count = 0
result = 0
while True:
    sq = n**2
    n += 1
    if sq % 10 != 9:
        continue
    elif (sq % 1000)/100 != 8:
        continue
    elif (sq % 100000)/10000 != 7:
        continue
    elif (sq % 10000000)/1000000 != 6:
        continue
    elif (sq % 1000000000)/100000000 != 5:
        continue
    elif (sq % 100000000000)/10000000000 != 4:
        continue
    elif (sq % 10000000000000)/1000000000000 != 3:
        continue
    elif (sq % 1000000000000000)/100000000000000 != 2:
        continue
    elif (sq % 100000000000000000)/10000000000000000 != 1:
        continue
    else:
        result = (n-1)*10
        break

print "result %s returned in %s seconds" % (result, time.time()-start)
