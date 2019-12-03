#!/usr/bin/python
# Advent of Code Day 2, Problem 2
# Solves (https://adventofcode.com/2019/day/2) given input.txt on the same path.

# Ingest input.txt treating the comma-separated items like stack registers 
# OPCODE 1 = (ADD, pointer_to_val1, pointer_to_val2, addr_to_store_result)
# OPCODE 2 = (MULT, pointer_to_val1, pointer_to_val2, addr_to_store_result)
# OPCODE 99 = HALT, takes no parameters 
# Find the arguments at input[1] and input[2] that set input[0] to 19690720

import os

# Sets a cross-platform relative folder so this script can run wherever
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
file_location = os.path.join(THIS_FOLDER, 'input.txt')

def filehandler():
    with open(file_location, "r") as inputfile:
        while inputfile:
            inputline = inputfile.readline()
            if inputline:
                assembly = list(map(int, inputline.split(",")))
            else:
                break
    return assembly

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

    >>> oper([3, 6, 9, 12, 99], 0)
    ERROR: unrecognized opcode 3 at 0
    [3, 6, 9, 12, 99]

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

def main():
    # Initialize constants:
    turing_tape = filehandler()             # Build Turing Tape from the input file
    original_values = list(turing_tape)     # Keep a clean copy of this list using list()
    loopsize = 99                           # Per problem definition, NOUN & VERB are in range [0 .. 99] inclusive
    goal_value = 19690720                   # Per problem definition 
    noun = 0                                # Set up loop
    while(noun <= loopsize):
        verb = 0
        while(verb <= loopsize):
            turing_tape = list(original_values)
            turing_tape[1] = noun
            turing_tape[2] = verb
            output = oper(turing_tape, 0)
            if(turing_tape[0] == goal_value):
                # Reporting an answer of the form [(noun * 100) + verb]
                print("A = {}, B = {}, REPORT ANSWER {}".format(noun, verb, (noun*100) + verb))
                return(output)
                break
            else:
                print(turing_tape[0], turing_tape[1], turing_tape[2], turing_tape[3]) 
            verb += 1
        noun += 1
    return(output)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    answer = main()
    print(answer)