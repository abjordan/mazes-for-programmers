#!/usr/bin/env python3

from grid import Grid

class DistanceGrid(Grid):

    def to_base36(self, num):
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        idx = abs(num % len(alphabet))
        return alphabet[idx]
    
    def contents_of(self, cell):
        if self.distances and cell in self.distances.keys():
            return self.to_base36(self.distances[cell])
        else:
            return super().contents_of(cell)
