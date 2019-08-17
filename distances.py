#!/usr/bin/env python3

class Distances:
    def __init__(self, root):
        self.root = root
        self.cells = {}
        self.cells[root] = 0

    def __getitem__(self, cell):
        if not cell in self.cells.keys():
            raise KeyError("Cell is not in distances")
        return self.cells[cell]

    def __setitem__(self, cell, value):
        self.cells[cell] = value
        
    def cells(self):
        return self.cells

    def keys(self):
        return self.cells.keys()

    def path_to(self, goal):
        current = goal
        
        breadcrumbs = Distances(self.root)
        breadcrumbs[current] = self.cells[current]

        while current != self.root:
            for neighbor in current.links():
                if self.cells[neighbor] < self.cells[current]:
                    breadcrumbs[neighbor] = self.cells[neighbor]
                    current = neighbor
                    break

        return breadcrumbs
