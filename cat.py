"""
i = 1
length = 3
while i < length:
     num = i + 1
     print(f"{num} meow")
     i += 1
"""

# print("meow\n" * 3, end="")

"""
n = abs(int(input("Enter n: ")))

for i in range(n):
    num = i + 1
    print(f"{num} meow")
"""

def main():

    n = getNumber()
    meow(n)
    

def getNumber():
    while True:
        n = int(input("Enter n: "))
        if n > 0:
            return n
        else: 
            print("Please enter a positive number.")
            continue

def meow(n):
    for _ in range(n):
        print("meow")

main()