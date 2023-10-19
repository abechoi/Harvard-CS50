# x = float(input("Enter X: "))
# y = float(input("Enter Y: "))

# round(number[, ndigits])
# [, ndigits] = optional
# z = round(x + y)

# f"{z:,}" = formats z with commas
#print(f"{z:,}")

# z = x / y

# f"{z:.2f}" = formats z with 2 decimal places
# print(f"{z:.2f}")

# z = round(x / y, 2) # round to 2 decimal places

def main():
    x = int(input("Enter X: "))
    print("X squared =", square(x))

def square(x):
    return x ** 2

if __name__ == "__main__" :
    main()