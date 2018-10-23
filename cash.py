from cs50 import get_float

# Prompt user for change owed
while True:
    change = get_float("Change owed: ")
    if change >= 0:
        break

# Convert to total cents owed
cents = round(change*100)

# Get amount of quarters then update cents left
q = cents // 25
cents = cents % 25

# Get amount of dimes then update cents left
d = cents // 10
cents = cents % 10

# Get amount of nickels then update cents left
n = cents // 5
cents = cents % 5

# Get amount of pennies
p = cents

# Give minimum number of coins
print(f"{(q+d+n+p)}")
