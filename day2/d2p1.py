#!/usr/bin/python
# Advent of Code Day 2, Problem 1
# Solves (https://adventofcode.com/2019/day/2) given input.txt on the same path.

# Ingest input.txt treating the comma-separated items like stack registers 
# OPCODE 1 = (ADD, pointer_to_val1, pointer_to_val2, addr_to_store_result)
# OPCODE 2 = (MULT, pointer_to_val1, pointer_to_val2, addr_to_store_result)
# OPCODE 99 = HALT, takes no parameters 

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
                output = oper(turing_tape, int(0)) 
            else:
                break
    print(output)
    return

def oper(stack: int, pointer: int):
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

    >>> oper([69, 420, 90210, 0, 99], 0)
    ERROR: tried to read out of bounds
    [69, 420, 90210, 0, 99]

    >>> oper([69, 1, 1, 0, 99], 0)
    ERROR: unrecognized opcode 69 at 0
    [69, 1, 1, 0, 99]

    """
    while (pointer < len(stack)):
        opcode = stack[pointer]
        if (opcode == 99):
            print("Reached HALT instruction at {}".format(pointer))
            break
        try:
            eax = stack[(stack[pointer+1])]
            ebx = stack[(stack[pointer+2])]
            addr = stack[pointer+3]
        except IndexError:
            print("ERROR: tried to read out of bounds")
            break
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