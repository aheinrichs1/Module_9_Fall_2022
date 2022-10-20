"""
Program: dictionary_ops.py
Author: Alex Heinrichs
Date Created: 10/20/2022

Contaions a function that accepts a dictionary
and prints the pairs (key, value) one per line
(taken from my_definitions.py)
"""


def print_dict(input_dict):
    """
    Takes a dictionary parameter and prints its contents
    :param input_dict: dictionary to be printed
    """
    for key in input_dict:
        print("Key:", key, "Value:", input_dict[key])
