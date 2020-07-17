"""Reverse a string"""
from string import *

str1 = input("Enter a string:")

"""
def reverse_string(s):
    return s[::-1]


print("Reverse of a string:", reverse_string(str1))
"""


def reverse_string(s):
    str2 = ""
    for i in s:
        str2 = i + str2
    return str2


print("Reverse of a string:", reverse_string(str1))
