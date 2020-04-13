import sys, pygame
import pandas as pd

pygame.init()

class SQUARE:
    POSITION = { 'x': 0, 'y': 0 }
    DIMENSIONS = { 'x': 64, 'y': 64 }
    COLOR = { 'r': 0, 'g': 0, 'b': 0 }

    def __init__(self, position, dimensions, color):
        self.POSITION = position
        self.DIMENSIONS = dimensions
        self.COLOR = color
        print('CREATED NEW SQUARE WITH: \nPOSITION: \t%s\DIMENSIONS: \t%s\COLOR: \t%s\n\n' % (str(self.POSITION), str(self.DIMENSIONS), str(self.COLOR)))


    def drawSquare(self, screen, square):
        pygame.draw.rect(screen, square['color'], square)
        pass
