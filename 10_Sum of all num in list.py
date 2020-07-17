"""Sum of all numbers in list"""

li = []
n = int(input("Enter the length  of list:"))
for i in range(0, n):
    ele = int(input('Enter the value:'))
    li.append(ele)
print("Elements in the list:", li)


def add_list(l):
    sum1 = 0
    for j in l:
        sum1 += j
    return sum1


print("Sum of elements in list:", add_list(li))
