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


def createRobot(start):
    start = ((start[0] * 32) + 16, (start[1] * 32) + 16)
    da_robot = robo(screen, (0,255,0), start, 16, 'bottom')
    return da_robot


def loadMaze(new_maze, path):
    loaded_maze = new_maze.loadMaze(path)
    return loaded_maze

def findStartingPoint(layout):
    start = (0,0)
    for v_index, row in layout.iterrows():          # Row = top to bottom
        for index, col in enumerate(row):           # Col = left to right
            if col == 's':
                start = (index, v_index)
                break

    print("Found start at: %s" % str(start))
    return start


def startLoop():
    path_to_maze = '../examples/maze3.csv'
    new_maze = createMaze()
    maze_layout = loadMaze(new_maze, path_to_maze)
    new_maze.drawMaze(maze_layout)
    starting_point = findStartingPoint(maze_layout)
    robot = createRobot(starting_point)
    robot.drawRobot()

    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # robot.move((48, 48))

        # screen.fill(black)
        pygame.display.flip()


startLoop()