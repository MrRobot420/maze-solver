import sys, pygame

pygame.init()

class Maze:
    SQUARE_SIZE = 0
    TOTAL_SIZE = { 'x': 0, 'y': 0 }
    DIMENSIONS = { 'x': 0, 'y': 0 }

    def __init__(self, size, square_size, dimensions):
        self.TOTAL_SIZE = size
        self.SQUARE_SIZE = square_size
        self.DIMENSIONS = dimensions
        print('CREATED NEW MAZE WITH: \nTOTAL_SIZE: \t%s\nSQUARE_SIZE: \t%s\nSQUARE_SIZE: \t%s' % (str(self.TOTAL_SIZE), str(self.SQUARE_SIZE), str(self.DIMENSIONS)))


    def loadMaze(self, path):
        pass


    def drawMaze(self, maze):
        pass