import sys, pygame
from maze import Maze as mz
from robot import Robot as robo

pygame.init()
size = width, height = 512, 512
maze_size = { 'x': 512, 'y': 512 }
speed = [2, 0]                              # one has to be zero in order for it to move: left, right, top, down
black = 0, 0, 0
screen = pygame.display.set_mode(size)
da_maze = ''


def createMaze():
    da_maze = mz(screen, maze_size, { 'x': 32, 'y': 32 }, { 'x': 16, 'y': 16})
    return da_maze


def createRobot():
    da_robot = robo(screen, (0,255,0), (48,16), 16, 'bottom')
    return da_robot


def loadMaze(new_maze, path):
    loaded_maze = new_maze.loadMaze(path)
    return loaded_maze


def startLoop():
    new_maze = createMaze()
    maze_layout = loadMaze(new_maze, '../examples/maze3.csv')
    new_maze.drawMaze(maze_layout)
    robot = createRobot()
    robot.drawRobot()

    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # screen.fill(black)
        pygame.display.flip()


startLoop()