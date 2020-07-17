"""Pascal's triangle"""
'''
n = int(input("Enter the number: "))
a = []
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1, i):
        a[i].append(a[i - 1][j - 1] + a[i - 1][j])
    if n != 0:
        a[i].append(1)
for i in range(n):
    print(" " * (n - i), end=" ", sep=" ")
    for j in range(0, i + 1):
        print('{0:6}'.format(a[i][j]), end=" ", sep=" ")
    print()
'''
n = int(input("enter the size of tringle:"))


def pascal_triangle(t):
    a = [[] for i in range(n)]
    for i in range(n):
        for j in range(n + 1):
            if j < i:
                if j == 0:
                    a[i].append(1)
                else:
                    a[i].append(a[i - 1][j] + a[i - 1][j - 1])
            elif (j == i):
                a[i].append(1)
    return a


print("Pascal's triangle:", pascal_triangle(n), end='')
