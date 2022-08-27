def calcSum(lst):
    sumlst = lst.pop()
    if lst == []:
        return sumlst
    else:
        return calcSum(lst) + sumlst


lst = [2, 3, 8, 11, 4, 6]
print(calcSum(lst))


# Reverse order of summation
def calcSum(lst):
    sumlst = lst.pop(0)
    if lst == []:
        return sumlst
    else:
        return calcSum(lst) + sumlst


lst = [2, 3, 8, 11, 4, 6]
print(calcSum(lst))