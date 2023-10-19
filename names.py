names = []
    
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for names in sorted(names, reverse=True):
    print(f"Hello, {names}!")