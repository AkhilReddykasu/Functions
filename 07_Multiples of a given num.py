"""Multiples of a given number"""

num = int(input("enter a number to find the table:"))
def multiple(n):
    print("Multiples of a number",n,"are:")
    for i in range(1,11):
        print(n * i)



multiple(num)