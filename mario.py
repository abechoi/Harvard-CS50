def main():
    print_square(3, 6)


def print_square(row, column):
    """
    for i in range(row):
        for j in range(column):
            print("#", end="")
        print()
    """
    for _ in range(row):
        print_column(column)
    

def print_column(column):
    print("#" * column)

main()