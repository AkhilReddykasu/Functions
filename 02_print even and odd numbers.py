"""print even and odd numbers"""

def even():
    print("even numbers from 1 to 100:")
    for i in range(1,100):
        if i % 2 == 0:
            print(i)


even()

def odd():
    print("Odd numnbers from 1 to 100:")
    for i in range(1,100):
        if i % 2 != 0:
            print(i)

odd()


