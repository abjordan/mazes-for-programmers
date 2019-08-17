#!/usr/bin/env python

from distances import Distances

class Cell:

    row = None
    column = None
    my_links = None
    (north, south, east, west) = (None, None, None, None)
    
    def __init__(self, r, c):
        self.row = r
        self.column = c
        self.my_links = {}

    def link(self, cell, bidi=True):
        self.my_links[cell] = True
        if bidi:
            cell.link(self, False)
        return self

    def unlink(self, cell, bidi=True):
        self.my_links.remove(cell)
        if bidi:
            cell.unlink(self, false)
        return self

    def links(self):
        return self.my_links.keys()

    def is_linked(self, cell):
        return self.my_links.get(cell, False)

    def neighbors(self):
        ret = []
        if self.north: ret += self.north
        if self.south: ret += self.south
        if self.east: ret += self.east
        if self.west: ret += self.west

        return ret

    def distances(self):
        distances = Distances(self)
        frontier = [ self ]

        while len(frontier) is not 0:
            new_frontier = []
            for cell in frontier:
                for linked in cell.links():
                    if linked in distances.keys():
                        continue
                    distances[linked] = distances[cell] + 1
                    new_frontier.append(linked)
            frontier = new_frontier

        return distances
    
    def __str__(self):
        ret = "Cell at ({}, {}), linked to {} neighbors".format(
            self.row, self.column, len(self.my_links))
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

    c_dist = c.distances()
    for key in c_dist.keys():
        print(key, c_dist[key])
