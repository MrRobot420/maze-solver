import sys, pygame
import pandas as pd
import square

pygame.init()

class Maze:
    SQUARE_SIZE = 0
    TOTAL_SIZE = { 'x': 0, 'y': 0 }
    DIMENSIONS = { 'x': 0, 'y': 0 }

    def __init__(self, size, square_size, dimensions):
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
            for col in row:
                print('TYPE: %s' % str(col))

                if col == 'b':
                    #draw black
                    pass
                elif col == 'w':
                    #draw white
                    pass
                elif col == 's':
                    # draw orange
                    pass
                elif col == 'e':
                    # draw yellow
                    pass