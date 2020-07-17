"""check given word is palindrome or not"""


str1 = input("enter a string:")

def palindrome(a):
    if a == a[::-1] :
        print("string is a palindrome")
    else:
        print("not a palindrome")


palindrome(str1)

