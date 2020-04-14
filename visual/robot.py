import sys, pygame
import pandas as pd

class Robot:
    SCREEN = ''
    COLOR = (0,255,0)
    POSITION = (16, 16)
    RADIUS = 16
    DIRECTION = 'bottom'

    def __init__(self, screen, color, position, radius, direction):
        self.SCREEN = screen
        self.COLOR = color
        self.POSITION = position
        self.RADIUS = radius
        self.DIRECTION = direction

    
    def drawRobot(self):
        # player = pygame.Circle()
        pygame.draw.circle(self.SCREEN, self.COLOR, self.POSITION, self.RADIUS)