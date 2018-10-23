import sys
from sys import argv
from cs50 import get_string

# Have the user enter one command-line argument
if len(argv) != 2:
    sys.exit("Usage: caesar.py k")

# Convert the key into an integer
key = int(sys.argv[1])

# Prompt user for plaintext message
plaintext = get_string("plaintext: ")

# Print ciphered message
print("ciphertext: ", end="")

# Number of letters in the alphabet
number_of_letters = 26

# Encipher text
for c in plaintext:

    # Preserve case of letters and add key
    if str.islower(c):
        new_lowercase_letter = (ord(c) - ord('a') + key) % number_of_letters + ord('a')
        print(f"{chr(new_lowercase_letter)}", end="")
    elif str.isupper(c):
        new_uppercase_letter = (ord(c) - ord('A') + key) % number_of_letters + ord('A')
        print(f"{chr(new_uppercase_letter)}", end="")

    # Presere symbols and spaces
    else:
        print(f"{c}", end="")

# Print new line
print()