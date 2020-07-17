"""Fibonacci series"""

def fibonacci():
    num = int(input('enter the range:'))
    n1 , n2 = 0 , 1
    next = 0
    if num == 1:
        print(n1)
    else:
        while next < num:
            print(n1)
            n3 = n1 + n2
            n1 , n2 = n2 , n3
            next += 1
fibonacci()



def fib(n):
    if n == 0:
        print("No items")
    else:
        a = 0
        b = 1
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)

fib(10)
