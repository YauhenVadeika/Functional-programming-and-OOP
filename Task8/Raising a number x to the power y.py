def exponentiation(x, y):
    if y > 0:
        return x * exponentiation(x, y - 1)
    else:
        return 1


print(exponentiation(2, 3))
print(exponentiation(2, 2))
