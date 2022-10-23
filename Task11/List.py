"""Python style."""

""" Summary 

Given a list. All numbers in the list check for parity.
If the number is even then calculate the sum of the digits.
If odd then replace it with 1 in the list.
All words: count the number of vowels and consonants.
Display everything on the screen.

"""

# Method1
lst = [15, 48, "hello", 6, 19, "world"]

print(f"sumeven - {(sum([int(i) for i in lst if i != str(i) and i % 2 == 0]))}")
print(f"repnum - {[int(i / i) if i != str(i) and i % 2 != 0 else i for i in lst]}")
print("sumvowels -", vowels := (sum([len(i) for i in (str(lst)).lower() if i in "aeioue"])))
print("sumcons -", (abs(sum([len(i) for i in lst if i == str(i) and i not in "aeioue"])-vowels)))


# Method2
def stask(lst):

    sumeven = (sum([int(i) for i in lst if i != str(i) and i % 2 == 0]))
    repnum = ([int(i / i) if i != str(i) and i % 2 != 0 else i for i in lst])
    sumvowels = sum([len(i) for i in (str(lst)).lower() if i in "aeioue"])
    sumtotal = sum([len(i) for i in lst if i == str(i) and i not in "aeioue"])
    return f"sumeven - {sumeven}\nrepnum - {repnum}\nsumvowels - {sumvowels}\nsumcons - {abs(sumtotal-sumvowels)}"


print(stask([15, 48, "hello", 6, 19, "world"]))


# Method3
def sumeven(lst):
    print(f"sumeven - {sum([int(i) for i in lst if i != str(i) and i % 2 == 0])}")


def repnum(lst):
    print(f"repnum - {[int(i / i) if i != str(i) and i % 2 != 0 else i for i in lst]}")


def sumvowels(lst):
    return (sum([len(i) for i in (str(lst)).lower() if i in "aeioue"]))


def nsumcons(lst):
    sumeven(lst)
    repnum(lst)
    print(f"sumvowels - {sumvowels(lst)}")
    print("sumcons - ", (abs(sum([len(i) for i in lst if i == str(i) and i not in "aeioue"])) - sumvowels(lst)))


nsumcons([15, 48, "hello", 6, 19, "world"])
