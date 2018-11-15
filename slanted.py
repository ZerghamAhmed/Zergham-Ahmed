import sys
from cs50 import get_string

def main():

    # Ensure proper usage
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        exit("Usage: python slanted.py depth")
    depth = int(sys.argv[1])

    # Encrypt message
    message = get_string("Message: ")
    if len(message) >= depth:
        print("Slanted:", slant(message, depth))


def slant(message, depth):

    # Create a list to numerate each character
    A = list()

    # Create a list with each character
    index = 0
    while index < len(message):
        A.append(message[index])

    # Use step of range to select every second character and remove from first list
    for i in range(0, A, depth):
        B = list()
        A.pop(B)

    # rearrange by added second list to first, joining the list of separated characterss
    message = A.join + B.join
    print (A)
    print(B)
    return message

    # dd this list of every second character to the first list of every other character

    #also had the idea of using substrings and then adding them up


    # A = list()
    # for i in range(len(message) - depth + 1):

    #     # Extract substrings by slicing
    #     A.append(message[i:i+depth])

    # # tokenize by each letter in each substring
    # for i in range(0, len(A), len(A)-(depth-1):

##https://www.pythonlearn.com/html-008/cfbook007.html

if __name__ == "__main__":
    main()