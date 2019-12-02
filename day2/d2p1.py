#!/usr/bin/python
# Advent of Code Day 2, Problem 1
# Solves (https://adventofcode.com/2019/day/2) given input.txt on the same path.

# Ingest input.txt line by line, treating the entries as integers ("mass")
# Perform a straightforward piece of arithmetic on them ("fuel requirements")
# Sum the results and return the output

import math
import os

# Sets a cross-platform relative folder so this script can run wherever
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
file_location = os.path.join(THIS_FOLDER, 'input.txt')

def main():
    with open(file_location, "r") as inputfile:
        while inputfile:
            inputline = inputfile.readline()
            if inputline:
                turing_tape = inputline.split(",")
                # DO STUFF 
            else:
                break
    
    return

def oper(stack, stack_pointer):
    """
    :param list: a list including at least 4 items
    :param stack_pointer: an int pointing to an element of the list 

    >>> code = [1, 0, 0, 0, 99]; (outcode, pointer) = oper(code, 0); outcode
    [2, 0, 0, 0, 99]

    """
    while stack:
        opcode = stack_pointer
        eax = stack_pointer+1 # TODO: Fix buffer underrun error!
        ebx = stack_pointer+2
        addr = stack_pointer+3    
        if (opcode == 1):   # ADD EAX, EBX @ ADDR
            stack[addr] = eax + ebx
        elif (opcode == 2): # MULT EAX, EBX @ ADDR
            stack[addr] = eax * ebx
        elif (opcode == 99): # HALT
            print("Reached HALT instruction at {}".format(addr))
            break
        else:
            print("ERROR: unrecognized opcode {} at {}".format(opcode, addr))
            break
        stack_pointer += 4
    return(stack)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()