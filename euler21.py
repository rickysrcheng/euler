__author__ = 'TwoZer0Nine'


def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

lst = []

for i in xrange(2, 10001):
    a = factors(i)
    Sum = 0
    for j in a:
        Sum += j
    Sum -= i

    b = factors(Sum)
    other_sum = 0
    for k in b:
        other_sum += k
    other_sum -= Sum

    if other_sum == i and other_sum != Sum and other_sum not in lst: #and Sum not in lst:
        lst.append(Sum)
        lst.append(other_sum)

result = 0

for j in lst:
    result += j

print lst, result


