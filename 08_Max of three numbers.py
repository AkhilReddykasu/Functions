"""Maximum number out of three numbers"""

li1 = [9, 999, 99]


def maximum(l):
    li1.sort(reverse=True)
    return l[0]


print("maximum num in list li:", maximum(li1))



li2 = [7,8,9,4,5]
def maxi(l):
    print("maximum number in list", max(l))


maxi(li2)
