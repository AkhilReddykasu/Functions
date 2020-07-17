"""Factorial of a number"""

num = int(input("enter a number to find a factorial:"))
def fact(n):
    i = 1
    for j in range(1,n+1):
        i = i * j
    return i


print("Factorial of",num,"is:",fact(num))