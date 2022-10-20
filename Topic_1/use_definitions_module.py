"""
Module: use_definitions_module.py
Author: Alex Heinrichs
Date Created: 10/20/2022

Module that contains a main function to test out code from
my_definitions.py
"""
import my_definitions


if __name__ == '__main__':
    my_definitions.greeting()
    my_definitions.print_author()
    user_dict = {'Name': 'Alex', 'Age': 68, 'Honesty': 'iffy'}
    my_definitions.print_dict(user_dict)
    user_set = ('wow', 'it works!', 'Python is friggen cool!')
    my_definitions.print_set(user_set)
