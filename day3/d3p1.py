#!/usr/bin/python
# Advent of Code Day 3, Problem 1
# Solves (https://adventofcode.com/2019/day/3) given input.txt on the same path.

# Ingest input.txt treating the comma-separated items as wiring guides
# Find the shortest Manhattan distance to a place where the wires cross

import os

# Sets a cross-platform relative folder so this script can run wherever
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
file_location = os.path.join(THIS_FOLDER, 'input.txt')

def filehandler(file_location):
    with open(file_location, "r") as inputfile:
        wiring = list()
        for line in inputfile:
            # From each line, strip newlines, and split comma-separated elements into a list
            wiring.append(list(line.rstrip().split(","))) 
    return wiring

def follow_segment(segment, x_start, y_start):
    """
    :param segment: a string of the form Lnnn where L is a letter U/D/L/R and nnn is an integer
    :param x_start: an integer for the starting x coordinate
    :param y_start: an integer for the starting y coordinate

    >>> follow_segment("R5", -2, 9)
    [[-2, 9], [-1, 9], [0, 9], [1, 9], [2, 9]]

    """
    wired_points = list()
    direction = segment[0]
    magnitude = int(segment[1:])
    if (direction == "U"):
        vector = [0, 1]
    elif (direction == "D"):
        vector = [0, -1]
    elif (direction == "L"):
        vector = [-1, 0]
    elif (direction == "R"):
        vector = [1, 0]
    else:
        print("ERROR: non-cardinal direction of {}".format(direction))
        return -1
    for i in range(magnitude):
        wired_points.append([x_start + i * vector[0], y_start + i * vector[1]])
    return wired_points

def follow_wire(routing_list):
    """
    :param routing_list: a string of segments of the form Lnnn where L is a letter U/D/L/R, and nnn is an integer
    """
    wire = list()
    wire.append([0, 0])
    for segment in routing_list:
        coords = list.(wire[-1:])  # TODO: figure out how to get x and y off the end of the list
        x_start = coords[0]
        y_start = coords[1]
        wire.append(follow_segment(segment, x_start, y_start))
    return wire
    
def main():
    wiring = filehandler(file_location)
    green_wire = follow_wire(wiring[0])
    red_wire = follow_wire(wiring[1])
    return

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()