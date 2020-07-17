"""Takes a list and returns a new list with unique elements of the first list."""

lst = []
len = int(input("Enter the size of list:"))
for i in range(0, len):
    ele = int(input("enter the elements into the list:"))
    lst.append(ele)
print("Elements before returning the unique values in list", lst)

"""
def unique_ele(lst1):

    return list(set(lst1))


print("Elements after returning the unique values in list:", unique_ele(lst))
"""


def unique_ele(lst1):
    x = []
    for i in lst1:
        if i not in x:
            x.append(i)
    return x


print("Elements after returning the unique values in list:", unique_ele(lst))
