#!/usr/bin/env python

import grid
import sys

if __name__=="__main__":

    import argparse

    from tree import BinaryTree
    from sidewinder import Sidewinder
    from distancegrid import DistanceGrid
    choices = ["tree", "sidewinder"]

    parser = argparse.ArgumentParser(description='Maze maker')
    parser.add_argument('-r', '--rows', default=8, help='Number of rows', type=int)
    parser.add_argument('-c', '--cols', default=8, help='Number of columns', type=int)
    parser.add_argument('-a', '--algo', metavar="ALGO", default=choices[0],
                        choices=choices, help=('Algorithm to use: ' + ', '.join(choices)))
    parser.add_argument('-d', '--djikstra', action="store_true", default=False,
                        help='Print distances in grid')
    parser.add_argument('-p', '--path', action='store_true', default=False,
                        help='Print solution path')

    parser.add_argument('--ascii', default=False, action='store_true', help='Print to terminal')
    parser.add_argument('--png', metavar="FILE", help='Output maze as a PNG to FILE')

    args = parser.parse_args()

    if args.djikstra:
        grid = DistanceGrid(args.rows, args.cols)
    else:
        grid = grid.Grid(args.rows, args.cols)
    maze = None
    if args.algo == "tree":
        maze = BinaryTree().on(grid)
    elif args.algo == "sidewinder":
        maze = Sidewinder().on(grid)

    if args.djikstra:
        start = grid[grid.rows-1,0]
        distances = start.distances()
        maze.distances = distances

        if args.path:
            maze.distances = distances.path_to(grid[ 0, grid.columns - 1 ])
                
    if args.ascii:
        print(maze.ascii())

    if args.png:
        maze.to_png(args.png)
        
        

    
