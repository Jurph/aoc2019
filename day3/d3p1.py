#!/usr/bin/python
# Advent of Code Day 3, Problem 1
# Solves (https://adventofcode.com/2019/day/3) given input.txt on the same path.

# Ingest input.txt treating the comma-separated items as wiring guides
# Find the shortest Manhattan distance to a place where the wires cross

import math
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


class Point(object):
    """ 
    Creates a point on a coordinate plane with values x & y.
    """

    def __init__(self, init_x, init_y):
        """
        Initialize a point's X and Y values
        """
        self.x = init_x
        self.y = init_y

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __add__(self, point):
        return Point((self.x + point.x), (self.y + point.y))

    def __sub__(self, point):
        return self + -point

    def __str__(self):
        return "Point({},{})".format(self.x, self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

    def manhattan(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return abs(dx) + abs(dy)

    def fromlist(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        return self

    def tolist(self, coordinates):
        coordinates[0] = self.x
        coordinates[1] = self.y
        return coordinates

def follow_segment(segment: str, origin: Point):
    """
    :param segment: a string of the form Lnnn where L is a letter U/D/L/R and nnn is an integer
    :param x_start: an integer for the starting x coordinate
    :param y_start: an integer for the starting y coordinate

    >>> p1 = Point(-2,9); follow_segment("R5", p1)
    [[-2, 9], [-1, 9], [0, 9], [1, 9], [2, 9]]

    """
    x_start = origin.getX()
    y_start = origin.getY()
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
    offset_x, offset_y = vector[0], vector[1]
    for i in range(magnitude):
        next_point = Point(int(x_start + offset_x * i), int(y_start+ offset_y * i))
        wired_points.append(next_point)
    return wired_points

def follow_wire(routing_list):
    """
    :param routing_list: a string of segments of the form Lnnn where L is a letter U/D/L/R, and nnn is an integer
    """
    wire = list()
    origin = Point(0,0)
    wire.append(origin)
    for segment in routing_list:
        coords = wire[-1:]
        startpoint = Point(coords[0], coords[1])
        wire.append(follow_segment(segment, startpoint)) # Recursion!!
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