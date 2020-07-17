"""Function to check whether a string is a pangram or not"""

str = input("Enter a string:")

def pangram(s):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in s.lower():
            return False

    return True


print('Checking whether a string is a pangram or not : ', pangram(str))
