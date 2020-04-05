#!/usr/bin/env python

import sys
from . import model, helper

def main_menu(arguments):

    while True:
        helper.clear_screen()
        helper.print_menu()
        user_input = input()
        switch = {
            '1':'subtraction',
            '2':'multiplication',
            '3':'random_number',
            '4':'sort_descending',
            '5':'sort_ascending'
        }

        func = switch.get(user_input, "invalid_choice")
        if func != "invalid_choice":
            result = getattr(model, func)(arguments)
            getattr(helper, func)(result)
        else:
            getattr(helper, func)()
        input("Press Enter to continue...")

def main(args):
    if len(args) < 7:
        helper.usage()
        sys.exit(1)

    args.pop(0)
    try:
        numbers = model.parse(args)
        main_menu(numbers)
    except ValueError as error:
        helper.eerror(error)
        helper.usage()
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv)
