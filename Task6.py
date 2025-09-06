row = int(input("Enter the number of rows:"))

for x in range(1, row + 1):
    for space in range(row - x):
        print(" ", end="")
    for star in range(2 * x - 1):
        print("*", end="")
    print()