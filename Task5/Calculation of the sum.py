def calcSum(lst):
    res = 0
    for i in lst:
        if not isinstance(i, list):
            res = res + i
        else:
            res = res + calcSum(i)
    return res


lst = [-2, 3, 8, 11, [-4, 6, [2, [-5, 4]]]]
print(calcSum(lst))
