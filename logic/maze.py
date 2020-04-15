import sys, pygame
import pandas as pd
from square import Square as sq

pygame.init()

class Maze:
    SCREEN = None
    SQUARE_SIZE = 0
    TOTAL_SIZE = { 'x': 64, 'y': 64 }
    DIMENSIONS = { 'x': 8, 'y': 8 }

    def __init__(self, screen, size, square_size, dimensions):
        self.SCREEN = screen
        self.TOTAL_SIZE = size
        self.SQUARE_SIZE = square_size
        self.DIMENSIONS = dimensions
        print('CREATED NEW MAZE WITH: \nTOTAL_SIZE: \t%s\nSQUARE_SIZE: \t%s\nMAZE_SIZE: \t%s\n\n' % (str(self.TOTAL_SIZE), str(self.SQUARE_SIZE), str(self.DIMENSIONS)))


    def loadMaze(self, path):
        maze_df = pd.read_csv(path, index_col=None, header=None)
        print(maze_df)
        return maze_df

    
    def createSquare(self, position, color):
        return sq(position, self.SQUARE_SIZE, color)


    def drawMaze(self, maze):
        for v_index, row in maze.iterrows():        # Row = top to bottom
            for index, col in enumerate(row):       # Col = left to right
                position = { 'x': index, 'y': v_index }

                if col == 'b':
                    new_square = self.createSquare(position, (0,0,0))             # draw black
                elif col == 'w':
                    new_square = self.createSquare(position, (255,255,255))       # draw white
                elif col == 's':
                    new_square = self.createSquare(position, (255,165,0))         # draw orange
                elif col == 'e':
                    new_square = self.createSquare(position, (255,215,0))         # draw yellow
                
                new_square.drawSquare(self.SCREEN)