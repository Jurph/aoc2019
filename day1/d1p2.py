#!/usr/bin/python
# Advent of Code Day 1, Problem 2
# Solves (https://adventofcode.com/2019/day/1#part2) given input.txt on the same path.
# Adds the Rocket Equation wrinkle: fuel requires fuel!

# Ingest input.txt line by line, treating the entries as integers ("mass")
# Perform a straightforward piece of arithmetic on them ("fuel requirements")
# Sum the results and return the output

import math
import os

# Sets a cross-platform relative folder so this script can run wherever
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
file_location = os.path.join(THIS_FOLDER, 'input.txt')

# Business logic for fuel calculations 
def calculatefuel(part_mass_in_kilos: int):
    """
    :param: part_mass_in_kilos is an integer 
    :return: fuel_mass_in_kilos is also an integer 
    """

    """
    # These are the unit tests as specified 

    >>> calculatefuel(12)
    2
    
    >>> calculatefuel(14)
    2

    >>> calculatefuel(1969)
    966

    >>> calculatefuel(100756)
    50346
    """
    fuel_total_in_kilos = 0
    fuel_mass_in_kilos = int(math.floor(part_mass_in_kilos/3) - 2)
    fuel_total_in_kilos += fuel_mass_in_kilos    
    if (fuel_mass_in_kilos > 0):
        fuel_total_in_kilos += calculatefuel(fuel_mass_in_kilos)
    else:
        return 0
    return int(fuel_total_in_kilos)

# Handles file I/O and delegates the math 
def main():
    required_fuel = 0
    with open(file_location, "r") as inputfile:
        while inputfile:
            inputline = inputfile.readline()
            if inputline:
                part_mass_in_kilos = int(inputline)
                fuel_mass_in_kilos = calculatefuel(part_mass_in_kilos)
                required_fuel += fuel_mass_in_kilos
            else:
                break
    print("Required fuel is {} kg".format(required_fuel))
    return int(required_fuel)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()