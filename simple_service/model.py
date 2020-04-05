#!/usr/bin/env python

import json
import random

def subtraction(args):
    return [num-1 for num in  args]

def multiplication(args):
    result = args[0]
    for number in args[1:]:
        result = result * number
    data_set = {}
    data_set['Numbers'] = args
    data_set['Multiplication'] = result
    json_object = json.loads(json.dumps(data_set))
    return json_object

def sort_ascending(args):
    return sorted(args)

def sort_descending(args):
    sorted_list = sort_ascending(args)
    sorted_list.reverse()
    return sorted_list

def random_number(args):
    return random.choice(args)

def parse(args):
    try:
        return list(map(int, args))
    except ValueError as error:
        raise error
