import math


def conv(dec, bin):

    if dec > 0:
        t = dec % 2
        return conv(dec // 2, bin + 1) + int(t * math.pow(10, bin))
    else:
        return 0


print(conv(126, 0))
