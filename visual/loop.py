import sys, pygame
from maze import Maze as mz

pygame.init()
size = width, height = 512, 512
maze_size = { 'x': 512, 'y': 512 }
speed = [2, 0]                              # one has to be zero in order for it to move: left, right, top, down
black = 0, 0, 0
screen = pygame.display.set_mode(size)
da_maze = ''


def createMaze():
    da_maze = mz(screen, maze_size, { 'x': 64, 'y': 64 }, { 'x': 8, 'y': 8})
    return da_maze


def loadMaze(new_maze, path):
    loaded_maze = new_maze.loadMaze(path)
    return loaded_maze


def startLoop():
    new_maze = createMaze()
    maze_layout = loadMaze(new_maze, '../examples/maze2.csv')
    new_maze.drawMaze(maze_layout)

    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # screen.fill(black)
        pygame.display.flip()


startLoop()