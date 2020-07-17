"""Multiply all the numbers in a list"""


li = []
n = int(input("Enter the length  of list:"))
for i in range(0, n):
    ele = int(input('Enter the value:'))
    li.append(ele)
print("Elements in the list:", li)


def Mul_list(l):
    mul1 = 1
    for j in l:
        mul1 *= j
    return mul1


print("Multiplication of elements in list:", Mul_list(li))