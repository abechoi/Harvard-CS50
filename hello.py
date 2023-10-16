"""
PRINT FUNCTION
*objects - Any number of objects separated by commas.
sep=' ' - Objects are separated by sep.
end='\n' - A string appended after the last object, by default a newline.
file=sys.stdout - An object with a write method. Defaults to the current sys.stdout.
flush=False - A Boolean, specifying if the output is flushed (True) or buffered (False). Defaults to False.
"""
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# Ask user for their name
# Remove whitespaces from str and capitalize first letter
# name = input("What's your name? ").strip().title()

# Split user's name by space into first and last name
# first, last = name.split(" ")


# Say hello to user
# print(f"hello, {first} {last}!")

# print("hello, ", name)
# print(f"hello, {name}!")
# print("hello, " + name + "!")
# print("hello, {}".format(name))

# print("hello, ", end="")
# print(name)

def main():
    name = input("What's your name? ")
    hello(name)

def hello(name="world"):
    name = name.strip().title()
    first, last = name.split(" ")
    print(f"hello, {first} {last}!")

main()