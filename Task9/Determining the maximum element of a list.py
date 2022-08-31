def maxnum(lst):
    if len(lst) > 1:
        max = maxnum(lst[1:])

        if lst[0] < max:
            return max
        else:
            return lst[0]

    if len(lst) == 1:
        return lst[0]


lst = [500, 2300, 800, 114, 36]
print(maxnum(lst))
