#!/usr/bin/env python

import sys
import json
from clear_screen import clear

def einfo(*args):
    print("[INFO] >>> ", *args)

def eerror(*args):
    print("[ERROR] >>> ", *args, file=sys.stderr)

def usage():
    eerror("Usage: please provide 6 consecutive integers as script parameters.")

def clear_screen():
    clear()

def subtraction(args):
    print(', '.join(map(str, args)))

def multiplication(args):
    print(args)
    filename = "multiplication_result.txt"

    with open(filename, 'w') as file:
        json.dump(args, file)
        einfo("Result saved in ", filename, ".")

def sort_ascending(args):
    print(args)

def sort_descending(args):
    print(args)

def random_number(args):
    print(args)

def parse_numbers():
    pass

def print_menu():
    text = """
    1. Subtraction 
    2. Multiplication
    3. Random number
    4. Print sorted (lowest to highest)
    5. Print sorted (highest to lowest)
    """
    print(text)

def invalid_choice():
    einfo("Invalid choice!")
        