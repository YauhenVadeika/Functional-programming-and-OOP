def quantNegnum(lst):

    if lst == []:
        return 0
    else:
        count = quantNegnum(lst[1:])
        if lst[0] < 0:
            count += 1
        return count


lst = [-2, 3, 8, -11, -4, 6]
print(quantNegnum(lst))


