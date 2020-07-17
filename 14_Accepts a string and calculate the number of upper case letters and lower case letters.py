"""Accepts a string and calculate the number of upper case letters and lower case letters"""

str1 = input("Enter a string:")


def string(s):
    upper = 0
    lower = 0
    for i in s:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        else:
            pass
    print("Number of upper case letters and lower case letters:")
    print("Upper =", upper)
    print("Lower =", lower)


string(str1)
