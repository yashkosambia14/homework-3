import pytest

from mypkg.my_answers import numbers_and_strings

def numbers_and_strings():
    """
    This is to review numbers and strings and basic operations.
    """
    # Write power of 2018
    x = 2018 ** 2

    # Assign a string "Stevens" to a variable y
    y = "Stevens"

    # Repeat variable y 5 times
    z = y * 5

    # What is the length of z?
    length = len(z)

    # Concatenate variable y with string " is good"
    m = y + " is good"

    # Replace "good" with "awesome" in variable m and assign it to a new variable n
    n = m.replace("good", "awesome")

    return x, y, z, length, m, n


