import math


def revNum(num):

    if num < 0:
        return -1

    if num == 0:
        return 0

    numdigit = 0
    numfin = num

    while numfin > 0:
        numdigit = numdigit + 1
        numfin = numfin // 10

    t = num % 10

    res = t * int(math.pow(10, numdigit - 1))

    return res + revNum(num // 10)


num = 123456789
print(revNum(num))
