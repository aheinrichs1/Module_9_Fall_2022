"""
Program: set_ops.py
Author: Alex Heinrichs
Date Created: 10/20/2022

Contains a function that accepts a set and prints the set
one item per line (taken from my_definitions.py)
"""


def print_set(input_set):
    """
    Takes a set parameter and prints its contents
    :param input_set: set to be printed
    """
    for value in input_set:
        print(str(value))
