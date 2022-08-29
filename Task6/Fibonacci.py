def Fibonacci(num, lst):

    count = len(lst)

    if len(lst) < 2:
        return []

    num1 = lst[count - 2]
    num2 = lst[count - 1]

    if (num1 + num2) < num:
        lst = lst + [num1 + num2]
        return Fibonacci(num, lst)
    else:
        return lst


print(Fibonacci(300, [0, 1]))
