#!/usr/bin/env python

class Cell:

    row = None
    column = None
    links = None
    (north, south, east, west) = (None, None, None, None)
    
    def __init__(self, r, c):
        self.row = r
        self.column = c
        self.links = {}

    def link(self, cell, bidi=True):
        self.links[cell] = True
        if bidi:
            cell.link(self, False)
        return self

    def unlink(self, cell, bidi=True):
        self.links.remove(cell)
        if bidi:
            cell.unlink(self, false)
        return self

    def links(self):
        return self.links.keys()

    def is_linked(self, cell):
        return self.links.get(cell, False)

    def neighbors(self):
        ret = []
        if self.north: ret += self.north
        if self.south: ret += self.south
        if self.east: ret += self.east
        if self.west: ret += self.west

        return ret

    def __str__(self):
        ret = "Cell at ({}, {}), linked to {} neighbors".format(
            self.row, self.column, len(self.links))
        return ret


if __name__=="__main__":

    c = Cell(0, 0)
    d = Cell(0, 1)
    e = Cell(0, 2)

    c.link(d)
    d.link(e)
    
    print("C: " + str(c))
    print("D: " + str(d))
    print("E: " + str(e))
