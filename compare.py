def main():
    x = int(input("Enter X: "))
    y = int(input("Enter Y: "))
    compare(x, y)

def compare(x, y):
    if x < y or x > y:
        print("X is not equal to Y")
    else:
        print("X is equal to Y")

    """
        if x < y:
            print("X is less than Y")
        elif x > y:
            print("X is greater than Y")
        else:
            print("X is equal to Y")
    """


main()