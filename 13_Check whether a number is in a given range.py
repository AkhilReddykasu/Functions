"""Check whether a number is in a given range"""

num = int(input("Enter the number:"))

def num_range(n):
    starting_num = 101
    ending_num = 1090
    if n > starting_num and n < ending_num :
        return "Given number is in range"
    else:
        return "Not in range"

print("Checking whether a number is in a given range:",num_range(num))









