#!/usr/bin/python3
# Advent of Code Day 4, Problem 1
# Solves (https://adventofcode.com/2019/day/1) given input.txt on the same path.

# Ingest input.txt line by line, treating the entries as integers ("mass")
# Perform a straightforward piece of arithmetic on them ("fuel requirements")
# Sum the results and return the output

import collections
import math
import os

def is_monotonic(six_digit_str):
    """
    >>> is_monotonic('123456')
    True

    >>> is_monotonic('111111')
    True

    >>> is_monotonic('223450')
    False

    """
    for digit in range(1, len(six_digit_str)):
        if (int(digit) == len(six_digit_str)): # If the counter we're on is about to exceed the length
            break
        elif(int(six_digit_str[int(digit)-1]) > int((six_digit_str[int(digit)]))):
            return False
        else:
            continue
    return True

def has_repeat(string_of_digits):
    """
    >>> has_repeat('123445')
    True

    >>> has_repeat('123123')
    False

    >>> has_repeat('111111')
    True

    """
    repeat_count = 0
    for digit in range(1, len(string_of_digits)):
        if (int(digit) == len(string_of_digits)): # If the counter we're on is about to exceed the length
            break
        elif(int(string_of_digits[int(digit)-1]) == int(string_of_digits[int(digit)])):
            repeat_count += 1
            break
        else:
            continue
    if (repeat_count > 0):
        return True
    else:
        return False
        
def has_threepeat(string_of_digits):
    """
    >>> has_threepeat('123445')
    False

    >>> has_repeat('121212')
    False

    >>> has_threepeat('111111')
    True

    >>> has_threepeat('111223')
    True

    >>> has_threepeat('113222')
    True

    """
    threepeat_count = 0
    for digit in range(2, len(string_of_digits)):
        if (int(digit) == len(string_of_digits)): # If the counter we're on is about to exceed the length
            break
        elif(int(string_of_digits[int(digit)-1]) == int(string_of_digits[int(digit)]) and 
             int(string_of_digits[int(digit)-2]) == int(string_of_digits[int(digit)])):
            threepeat_count += 1
            break
        else:
            continue
    if (threepeat_count > 0):
        return True
    else:
        return False

def sequence_length(check_string):
    """
    >>> sequence_length('111223')
    3

    >>> sequence_length('111231')
    3
    
    """
    count = {}
    for s in check_string:
        if s in count:
            count[int(s)] += 1
        else:
            count[int(s)] = 1
    final_count = sorted(count, reverse=True)
    return final_count[0]


def main():
    # Set up constants
    start_int = 134564
    end_int = 585159
    count = 0
    for candidate in range(start_int, end_int):
        if (is_monotonic(str(candidate)) and has_repeat(str(candidate))):
            if has_threepeat(str(candidate)):
                print("Candidate {} has a threepeat but may still be eligible".format(str(candidate)))
                continue
            else:
                count += 1
        else:
            continue
    print("Count was {}".format(count))
    return 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()