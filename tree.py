#!/usr/bin/env python

import random

class BinaryTree:

    def __init__(self):
        pass

    def on(self, grid):
        for cell in grid.each_cell():
            neighbors = []
            if cell.north: neighbors.append(cell.north)
            if cell.east:  neighbors.append(cell.east)

            if not len(neighbors) is 0:
                neighbor = random.choice(neighbors)
                if neighbor: cell.link(neighbor)

        return grid

if __name__=="__main__":
    import grid
    grid = grid.Grid(24,24)
    bt = BinaryTree()
    maze = bt.on(grid)
    print(maze.ascii())
    
    
            
                
