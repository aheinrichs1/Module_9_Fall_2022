"""
Module: use_definitions_module.py
Author: Alex Heinrichs
Date Created: 10/20/2022

Module that contains a main function to test out code from
my_definitions.py
"""

'''
Beta Test for self testing your homework; paste this at the bottom of your
use_definitions_module.py

Said another way, your code consuming your module should be above the three single quites
that are 4 lines up there ^

Note not all this code may be readable to you yet...it will come with time

Note only modify the mod_import line,don't touch the rest
'''
import my_definitions
import unittest
import builtins
import contextlib, io
from unittest.mock import Mock

# Note: Change this to what you called yourt import, such as
# import my_definitions as md
# then change it to md
mod_import = md


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class MyTestCase(unittest.TestCase):
    def test_greeting(self):
        # Mock the print statement
        mock = Mock()
        mock.side_effect = print
        print_original = print
        builtins.print = mock

        try:
            str_io = io.StringIO()
            with contextlib.redirect_stdout(str_io):
                mod_import.greeting()
            output = str_io.getvalue()

            # Check for print statement
            try:
                assert print.called
            except AssertionError:
                print(
                    f"{bcolors.WARNING}You appear to be missing a print statement within your greeting function." + bcolors.ENDC)
            # Check for empty print statement
            if len(output) < 3:
                print(f"{bcolors.WARNING}Your print statement is empty." + bcolors.ENDC)
            else:
                print(f"{bcolors.OKGREEN}Your greeting() function seems perfect." + bcolors.ENDC)
        except AttributeError:
            print(f"{bcolors.WARNING}Potentially missing a function defined as 'greeting()'." + bcolors.ENDC)
        finally:
            builtins.print = print_original

    def test_message(self):
        # Mock the print statement
        mock = Mock()
        mock.side_effect = print
        print_original = print
        builtins.print = mock

        try:
            str_io = io.StringIO()
            with contextlib.redirect_stdout(str_io):
                mod_import.message()
            output = str_io.getvalue()

            # Check for print statement
            try:
                assert print.called
            except AssertionError:
                print(
                    f"{bcolors.WARNING}You appear to be missing a print statement within your message function." + bcolors.ENDC)
            # Check for empty print statement
            if len(output) < 3:
                print(f"{bcolors.WARNING}Your print statement is empty." + bcolors.ENDC)
            else:
                print(f"{bcolors.OKGREEN}Your message() function seems perfect." + bcolors.ENDC)
        except AttributeError:
            print(f"{bcolors.WARNING}Potentially missing a function defined as 'message()'." + bcolors.ENDC)
        finally:
            builtins.print = print_original

    def test_print_dict(self):
        # Mock the print statement
        mock = Mock()
        mock.side_effect = print
        print_original = print
        builtins.print = mock

        a_dict = dict()
        a_dict['Test 1'] = 1
        a_dict['Test 2'] = 'Joe'
        a_dict['Test 3'] = 26.33
        a_dict['Test 4'] = ['a', 'small', 'list']

        try:
            str_io = io.StringIO()
            with contextlib.redirect_stdout(str_io):
                mod_import.print_dict(a_dict)
            output = str_io.getvalue()

            # Check for print statement
            try:
                assert print.called
            except AssertionError:
                print(
                    f"{bcolors.WARNING}You appear to be missing a print statement within your print_dict function; or one was never called." + bcolors.ENDC)
            if len(output) < 3:
                print(f"{bcolors.WARNING}Your print statement is empty." + bcolors.ENDC)
            else:
                if (output == "(Test 1, 1)\n(Test 2, Joe)\n(Test 3, 26.33)\n(Test 4, ['a', 'small', 'list'])\n"):
                    print(f"{bcolors.OKGREEN}Your print_dict() function seems perfect." + bcolors.ENDC)
                else:
                    split_text = output.split("\n")
                    print(f"{bcolors.WARNING}Some piece of your print statement didn't work" + bcolors.ENDC)
                    print(
                        f"{bcolors.WARNING}With a dictionary of a_dict = {{'Test 1':1, 'Test 2':'Joe', 'Test 3':26.33, 'Test 4': ['a','small','list']}}" + bcolors.ENDC)
                    print(f"{bcolors.WARNING}Expected output: " + bcolors.ENDC)
                    print(
                        f"{bcolors.OKBLUE}(Test 1, 1)\n(Test 2, Joe)\n(Test 3, 26.33)\n(Test 4, ['a', 'small', 'list']" + bcolors.ENDC)
                    print(f"{bcolors.WARNING}Actual output: " + bcolors.ENDC)
                    print(f"{bcolors.OKBLUE}{output}" + bcolors.ENDC)
        except AttributeError:
            print(f"{bcolors.WARNING}Potentially missing a function defined as 'print_dict()'." + bcolors.ENDC)
        except TypeError as te:
            if "positional arguments" in str(te):
                print(
                    f"{bcolors.WARNING}Potentially missing a parameter/argument for 'print_dict()'; should contain only 1 parameter." + bcolors.ENDC)
                print(f"{bcolors.WARNING}Original Error: \n\t" + str(te) + bcolors.ENDC)
            elif "can only concatenate str" in str(te):
                print(
                    f"{bcolors.WARNING}Dictionary print statement didn't handle values other than a dictionary of strings." + bcolors.ENDC)
                print(
                    f"{bcolors.WARNING}Suggestion: Add some type casting, such as casting an int to a string." + bcolors.ENDC)
                print(f"{bcolors.WARNING}Original Error: \n\t" + str(te) + bcolors.ENDC)
            else:
                print(f"{bcolors.WARNING}Uncaught use-case on my end. My bad." + bcolors.ENDC)
                print(f"{bcolors.WARNING}Original Error: \n\t" + str(te) + bcolors.ENDC)
        finally:
            builtins.print = print_original

    def test_print_set(self):
        # Mock the print statement
        mock = Mock()
        mock.side_effect = print
        print_original = print
        builtins.print = mock

        a_set = {'Apple', 'Banana', 6, 55.67}

        try:
            str_io = io.StringIO()
            with contextlib.redirect_stdout(str_io):
                mod_import.print_set(a_set)
            output = str_io.getvalue()

            # Check for print statement
            try:
                assert print.called
            except AssertionError:
                print(
                    f"{bcolors.WARNING}You appear to be missing a print statement within your print_set function; or one was never called." + bcolors.ENDC)
            if len(output) < 3:
                print(f"{bcolors.WARNING}Your print statement is empty." + bcolors.ENDC)
            else:
                # since sets are unordered
                if (4 == output.count(
                        '\n') and "Apple" in output and "Banana" in output and "6\n" in output and "55.67\n" in output):
                    print(f"{bcolors.OKGREEN}Your print_set() function seems perfect." + bcolors.ENDC)
                else:
                    split_text = output.split("\n")
                    print(f"{bcolors.WARNING}Some piece of your print statement didn't work" + bcolors.ENDC)
                    print(
                        f"{bcolors.WARNING}Note that sets are unordered to actual output might be in a different order than expected...that is fine." + bcolors.ENDC)
                    print(f"{bcolors.WARNING}With a set of a_set = {{'Apple', 'Banana',6,55.67}}" + bcolors.ENDC)
                    print(f"{bcolors.WARNING}Expected output: " + bcolors.ENDC)
                    print(f"{bcolors.OKBLUE}Apple\nBanana\n6\n55.67" + bcolors.ENDC)
                    print(f"{bcolors.WARNING}Actual output: " + bcolors.ENDC)
                    print(f"{bcolors.OKBLUE}{output}" + bcolors.ENDC)
        except AttributeError:
            print(f"{bcolors.WARNING}Potentially missing a function defined as 'print_set()'." + bcolors.ENDC)
        except TypeError as te:
            if "positional arguments" in str(te):
                print(
                    f"{bcolors.WARNING}Potentially missing a parameter/argument for 'print_set()'; should contain only 1 parameter." + bcolors.ENDC)
                print(f"{bcolors.WARNING}Original Error: \n\t" + str(te) + bcolors.ENDC)
            elif "can only concatenate str" in str(te):
                print(
                    f"{bcolors.WARNING}Dictionary print statement didn't handle values other than a dictionary of strings." + bcolors.ENDC)
                print(
                    f"{bcolors.WARNING}Suggestion: Add some type casting, such as casting an int to a string." + bcolors.ENDC)
                print(f"{bcolors.WARNING}Original Error: \n\t" + str(te) + bcolors.ENDC)
            else:
                print(f"{bcolors.WARNING}Uncaught use-case on my end. My bad." + bcolors.ENDC)
                print(f"{bcolors.WARNING}Original Error: \n\t" + str(te) + bcolors.ENDC)
        finally:
            builtins.print = print_original


if __name__ == '__main__':
    my_definitions.greeting()
    my_definitions.print_author()
    user_dict = {'Name': 'Alex', 'Age': 68, 'Honesty': 'iffy'}
    my_definitions.print_dict(user_dict)
    user_set = ('wow', 'it works!', 'Python is friggen cool!')
    my_definitions.print_set(user_set)
    unittest.main()
