import pytest

from mypkg.my_answer import dictionaries
def dictionaries():
    """
    This is to review basic operations with dictionaries.
    """
    # Create a dictionary that maps:
    #   fruit => "apple"
    #   quantity => 17
    #   color => "green"
    f = {"fruit": "apple", "quantity": 4, "color": "green"}

    # Get the item in dictionary f that the key "fruit" maps to
    a = f["fruit"]

    # Increase the quantity of f by 1
    f["quantity"] += 1

    # Create a nested dictionary where:
    #   name => {first_name => "Grace", last_name => "Hopper"} (a dictionary)
    #   jobs => ["scientist", "engineer"] (a list)
    #   age => 85
    amazing_grace = {"name": {"first_name": "Grace", "last_name": "hopper"},
                     "jobs": ["scientist", "engineer"],
                     "age": 85}

    # Add "programmer" to the list of jobs Grace has
    amazing_grace["jobs"].append("programmer")

    # Get the third job Grace has that you recently added
    p = amazing_grace["jobs"][-1]

    # Get the sorted keys of amazing_grace in alphabetically ascending order
    k = list(amazing_grace.keys())
    k.sort()

    return a, f, p, k





