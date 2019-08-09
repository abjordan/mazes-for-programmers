#!/usr/bin/env python

import random

from cell import Cell

class Grid:

    def __init__(self, rows, cols):
        self.rows = rows
        self.columns = cols
        self.cells = {}
        self.prepare_grid()
        self.configure_cells()

    def prepare_grid(self):
        for i in range(0, self.rows):
            self.cells[i] = {}
            for j in range(0, self.columns):
                self.cells[i][j] = Cell(i, j)
                
    def configure_cells(self):
        for r in self.cells:
            for c in self.cells[r]:
                cell = self.cells[r][c]
                cell.north = self[r - 1, c]
                cell.south = self[r + 1, c]
                cell.west  = self[r, c - 1]
                cell.east  = self[r, c + 1]

    def __getitem__(self, key):
        if not isinstance(key, tuple) or not len(key) is 2:
            raise IndexError("'{!r}' is not a valid grid index".format(key))
        r, c = key
        if r < 0 or r > (self.rows    - 1) : return None
        if c < 0 or c > (self.columns - 1) : return None
        
        return self.cells[r][c]

    def random_cell(self):
        r = random.choice(range(0, self.rows))
        c = random.choice(range(0, self.columns))
        return self.cells[r][c]
    
    def size(self):
        return self.rows * self.columns

    def each_row(self):
        for r in sorted(self.cells.keys()):
            yield self.cells[r]

    def each_cell_in_row(self, row):
        for c in sorted(row.keys()):
            yield row[c]
            
    def each_cell(self):
        for r in sorted(self.cells):
            for c in sorted(self.cells[r]):
                yield self.cells[r][c]

    def ascii(self):
        output = "+" + "---+" * self.columns + "\n"
        for row in sorted(self.cells):
            top = "|"
            bottom = "+"
            for col in sorted(self.cells[row]):
                cell = self.cells[row][col]

                body = "   "
                east = " " if cell.is_linked(cell.east) else "|"
                top += body + east

                south = "   " if cell.is_linked(cell.south) else "---"
                corner = "+"
                bottom += south + corner

            output += top + "\n"
            output += bottom + "\n"
        return output
                
if __name__=="__main__":
    g = Grid(4, 4)
    print(g[0,0])
    print(g.random_cell())
    
    print('------')
    for row in g.each_row():
        print(row)
    
    print('------')
    for cell in g.each_cell():
        print(cell)

    
