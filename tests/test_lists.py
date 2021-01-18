import pytest

from mypkg.fibonacci import fibonacci

def lists():
    """
    This is to review basic operations with lists.
    """
    n = "Stevens is awesome"

    # Split variable n on a delimiter space into a list of substrings
    p = n.split(" ")

    # Get all the items past the first of the third substring
    r = p[2][1:]

    # Create a 3 x 3 matrix as nested list such that
    #   first row is [1, 4, 5]
    #   second row is [6, 10, 11]
    #   third row is [12, 17, 38]
    A = [[1, 4, 5],
         [6, 10, 11],
         [12, 17, 38]]

    # Collect the items in the last column of matrix A using list comprehension
    c = [row[-1] for row in A]

    # Collect only the even items of the diagonal of matrix A using list comprehension
    d = [A[i][i] for i in range(len(A)) if A[i][i] % 2 == 0]

    # We can convert a single character to its underlying integer code (e.g., its ASCII byte value)
    # by passing it to the built-in ord function. Generate a list of these integers to represent
    # each character of the string "Stevens" using list comprehension.
    o = [ord(c) for c in "Stevens"]

    return p, r, c, d, o
