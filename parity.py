def main():
    x = int(input("Enter a number: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(x):
    # return True if x % 2 == 0 else False
    return x % 2 == 0

main()