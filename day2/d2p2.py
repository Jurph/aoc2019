#!/usr/bin/python
# Advent of Code Day 2, Problem 2
# Solves (https://adventofcode.com/2019/day/2) given input.txt on the same path.

# Ingest input.txt treating the comma-separated items like stack registers 
# OPCODE 1 = (ADD, pointer_to_val1, pointer_to_val2, addr_to_store_result)
# OPCODE 2 = (MULT, pointer_to_val1, pointer_to_val2, addr_to_store_result)
# OPCODE 99 = HALT, takes no parameters 
# Find the arguments at input[1] and input[2] that set input[0] to 19690720

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
                turing_tape = list(map(int, inputline.split(",")))
            else:
                break
    punch_cards = turing_tape # Write TT to cold storage
    a = 0
    b = 0
    while(a < 65535):
        while(b < 65535):
            turing_tape = punch_cards # Restore TT from backup
            turing_tape[1] = a # Set param 1 
            turing_tape[2] = b # Set param 2
            print("Trying {}, {}".format(a, b))
            output = oper(turing_tape, int(0))  # TODO: handle index out of range errors
            if(turing_tape[0] == 19690720):
                print("A = {}, B = {}, REPORT ANSWER {}".format(a, b, (a*100) + b))
                break
            else:
                b += 1
        a += 1
    
    print(output)
    return

def oper(stack, pointer):
    """
    :param list: a list including at least one OPCODE and parameters 
    :param pointer: an int pointing to an element of the list 

    >>> oper([1, 0, 0, 0, 99], 0)
    Reached HALT instruction at 4
    [2, 0, 0, 0, 99]

    >>> oper([2, 3, 0, 3, 99], 0)
    Reached HALT instruction at 4
    [2, 3, 0, 6, 99]

    >>> oper([2,4,4,5,99,0], 0)
    Reached HALT instruction at 4
    [2, 4, 4, 5, 99, 9801]

    >>> oper([1,1,1,4,99,5,6,0,99], 0)
    Reached HALT instruction at 8
    [30, 1, 1, 4, 2, 5, 6, 0, 99]

    """
    while (pointer < len(stack)):
        opcode = stack[pointer]
        if (opcode == 99):
            print("Reached HALT instruction at {}".format(pointer))
            break
        eax = stack[(stack[pointer+1])]
        ebx = stack[(stack[pointer+2])]
        addr = stack[pointer+3]
        if (opcode == 1):   # ADD EAX, EBX @ ADDR
            stack[addr] = eax + ebx
            pointer += 4
        elif (opcode == 2): # MULT EAX, EBX @ ADDR
            stack[addr] = eax * ebx
            pointer += 4
        else:
            print("ERROR: unrecognized opcode {} at {}".format(opcode, addr))
            break
    return(stack)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()