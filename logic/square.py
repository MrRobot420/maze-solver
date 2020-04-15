import sys, pygame
import pandas as pd

pygame.init()

class Square:
    POSITION = { 'x': 0, 'y': 0 }
    DIMENSIONS = { 'x': 64, 'y': 64 }
    COLOR = (0,0,0)
    START_POINT = { 'x': 0, 'y': 0 }
    END_POINT = { 'x': 64, 'y': 64 }

    def __init__(self, position, dimensions, color):
        self.POSITION = position
        self.DIMENSIONS = dimensions
        self.COLOR = color
        self.START_POINT['x'] = position['x'] * dimensions['x']
        self.START_POINT['y'] = position['y'] * dimensions['y']
        self.END_POINT['y'] = (position['y'] + 1) * dimensions['y']
        self.END_POINT['x'] = (position['x'] + 1) * dimensions['x']

        # print('CREATED NEW SQUARE WITH: \nPOSITION: \t%s\DIMENSIONS: \t%s\COLOR: \t%s\n\n' % (str(self.POSITION), str(self.DIMENSIONS), str(self.COLOR)))


    def drawSquare(self, screen):
        draw_square = pygame.Rect((self.START_POINT['x'], self.START_POINT['y']), (self.END_POINT['x'], self.END_POINT['y']))
        pygame.draw.rect(screen, self.COLOR, draw_square)
