"""print the even numbers from a given list"""


li =[]
length = int(input("Enter the length of list:"))
for i in range(0,length):
    ele = int(input("Enter the element:"))
    li.append(ele)
print("Elements in list:",li)


def even(l):
    li1 =[]
    for j in l:
        if j % 2 == 0:
            li1.append(j)
    return li1


print("Even elements in list:",even(li))











