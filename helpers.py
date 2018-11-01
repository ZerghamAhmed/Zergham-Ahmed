from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # Tokenize a and b, by lines, remove trailing \n, change each to set
    A = set(a.rstrip("\n").splitlines())
    B = set(b.rstrip("\n").splitlines())

    # Return intersection of sets and convert to list
    return list(A.intersection(B))


def sentences(a, b):
    """Return sentences in both a and b"""

    # Tokenize a and b, by sentences, change each to set
    A = set(sent_tokenize(a))
    B = set(sent_tokenize(b))

    # Return intersection of sets and convert to list
    return list(A.intersection(B))


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # Convert each to set, iterate over each string
    A = set()
    for i in range(len(a) - n + 1):

        # Extract substrings by slicing
        A.add(a[i:i+n])

    B = set()
    for i in range(len(b) - n + 1):
        B.add(b[i:i+n])

    # return intersection of the two sets
    return list(A.intersection(B))