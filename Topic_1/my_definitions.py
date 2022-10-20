"""
Module: my_definitions.py
Author: Alex Heinrichs
Date Created: 10/20/2022

Contains a set of definitions greeting(), print_author(),
print_dict(input_dict), and print_set(input_set) That will be called
by the module use_definitions_module.py to test working with
modules and imports
"""


def greeting():
    """
    Prints a greeting when called
    """
    print("Hello there, would you care for tea?")


def print_author():
    """
    Prints author of the module
    """
    print("The author of this code is Alex Heinrichs")


def print_dict(input_dict):
    """
    Takes a dictionary parameter and prints its contents
    :param input_dict: dictionary to be printed
    """
    for key in input_dict:
        print("Key:", key, "Value:", input_dict[key])


def print_set(input_set):
    """
    Takes a set parameter and prints its contents
    :param input_set: set to be printed
    """
    for value in input_set:
        print(str(value))
