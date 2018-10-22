from cs50 import get_int

# Prompt user for height between 1 and 8
while True:
    Height = get_int("Height: ")
    if Height > 0 and Height < 9:
        break

# Print out this many rows in range
for i in range(Height):

    # Print out spaces for this amount of columns in range
    for j in range(Height-(i+1)):
        print(" ", end="")

    # Print hashes in what are is left
    for k in range(i+1):
        print("#", end="")

    # Print new line
    print()

