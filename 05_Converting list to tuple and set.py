"""converting list to tuple and list"""



li = [4, 5, 2, 9, 6]

print("Before converting a list:",li)
def convert(l):
    print("After converting list to tuple:", tuple(l))
    print("After converting list to tuple:", set(l))


convert(li)


