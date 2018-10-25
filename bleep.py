from cs50 import get_string
from sys import argv
import sys


def main():

    banned_words = []
    # Prompt user for command-line argument for path of banned words dictionary
    if len(argv) != 2:
        print("Usage: python bleep.py dictionary")
        sys.exit(1)

    # Load dictionary of banned words
    else:
        dictionary = argv[1]
        file = open(dictionary, "r")

        # If failed to load, exit
        if not file:
            print("Could not open {}." .format(text))
            sys.exit(1)

        # Read dictionary, make words lowercase and strip trailing characters
        for line in file:
            banned_words.append(line.rstrip("\n").lower())
        file.close()

        # Prompt user for message, then split it into its components
        message = get_string("What message would you like to censor?\n")
        words_of_message = message.split()

        # Check if words are in dictionary
        for word in words_of_message:

            # Censor matched words
            if word.lower() in banned_words:
                print("*" * len(word), end=" ")
            else:
                print(word, end=" ")

    # Print new line
    print()


if __name__ == "__main__":
    main()
