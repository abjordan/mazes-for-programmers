#!/usr/bin/env python

import random

class Sidewinder:
    def on(self, grid):
        for row in grid.each_row():
            run = []
            for cell in grid.each_cell_in_row(row):
                run.append(cell)
                at_eastern_boundary = (cell.east is None)
                at_northern_boundary = (cell.north is None)

                should_close_out = (at_eastern_boundary or (not at_northern_boundary and (random.randint(0,1) == 0)))

                if should_close_out:
                    member = random.choice(run)
                    if member.north: member.link(member.north)
                    run = []
                else:
                    cell.link(cell.east)

        return grid

if __name__=="__main__":
    import grid
    import sys
    
    grid = grid.Grid(24, 24)
    sw = Sidewinder()
    maze = sw.on(grid)
    print(maze.ascii())

    maze.to_png(sys.argv[1])
