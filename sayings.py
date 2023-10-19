def hello(name):
    print(f"Hello, {name}!")

def goodbye(name):
    print(f"Goodbye, {name}!")

def main():
    hello("world")
    goodbye("world")

# __name__ = top-level code is being executed from command line
if __name__ == "__main__":
    main()