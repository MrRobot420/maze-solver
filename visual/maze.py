import sys, pygame
import pandas as pd
from square import Square as sq

pygame.init()

class Maze:
    SCREEN = None
    SQUARE_SIZE = 0
    TOTAL_SIZE = { 'x': 0, 'y': 0 }
    DIMENSIONS = { 'x': 0, 'y': 0 }

    def __init__(self, screen, size, square_size, dimensions):
        self.SCREEN = screen
        self.TOTAL_SIZE = size
        self.SQUARE_SIZE = square_size
        self.DIMENSIONS = dimensions
        print('CREATED NEW MAZE WITH: \nTOTAL_SIZE: \t%s\nSQUARE_SIZE: \t%s\nSQUARE_SIZE: \t%s\n\n' % (str(self.TOTAL_SIZE), str(self.SQUARE_SIZE), str(self.DIMENSIONS)))


    def loadMaze(self, path):
        maze_df = pd.read_csv(path, index_col=None, header=None)
        print(maze_df)
        return maze_df


    def drawMaze(self, maze):
        # Row = top to bottom
        for v_index, row in maze.iterrows():
            print('Row: %s' % str(row))
            # Col = left to right
            for index, col in enumerate(row):
                print('TYPE: %s' % str(col))

                if col == 'b':
                    #draw black
                    position = { 'x': index, 'y': v_index }
                    new_square = sq(position, { 'x':64, 'y': 64 }, (0,0,0))
                    new_square.drawSquare(self.SCREEN)
                elif col == 'w':
                    #draw white
                    position = { 'x': index, 'y': v_index }
                    new_square = sq(position, { 'x':64, 'y': 64 }, (255,255,255))
                    new_square.drawSquare(self.SCREEN)
                elif col == 's':
                    # draw orange
                    position = { 'x': index, 'y': v_index }
                    new_square = sq(position, { 'x':64, 'y': 64 }, (255,165,0))
                    new_square.drawSquare(self.SCREEN)
                elif col == 'e':
                    # draw yellow
                    position = { 'x': index, 'y': v_index }
                    new_square = sq(position, { 'x':64, 'y': 64 }, (255,215,0))
                    new_square.drawSquare(self.SCREEN)