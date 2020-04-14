import sys, pygame
from maze import Maze as mz
from robot import Robot as robo
import time

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
    da_robot = robo(screen, (0,255,0), start, 16, 'below', { 'x': 16, 'y': 16 })
    return da_robot


def loadMaze(new_maze, path):
    loaded_maze = new_maze.loadMaze(path)
    return loaded_maze

def findStartingPoint(layout):
    start = (0,0)
    for v_index, row in layout.iterrows():          # Row = top to bottom
        for index, col in enumerate(row):           # Col = left to right
            if col == 's':
                start = ((index * 32) + 16, (v_index * 32) + 16)
                break

    print("Found start at: %s" % str(start))
    return start


def checkEnvironment(old, layout, robot):
    index = (int((old[0] - 16) / 32), int((old[1] - 16) / 32))

    print('old index: ', index)
    left_block, above_block, right_block, below_block = 'b', 'b', 'b', 'b'

    if (index[0] >= 1):
        left_block = layout[index[0]-1][index[1]]
        print('left: %s' % left_block)
    if (index[1] >= 1):
        above_block = layout[index[0]][index[1]-1]
        print('above: %s' % above_block)
    if (index[0] < robot.DIMENSIONS['x']):
        right_block = layout[index[0]+1][index[1]]
        print('right: %s' % right_block)
    if (index[1] < robot.DIMENSIONS['y']):
        below_block = layout[index[0]][index[1]+1]
        print('below: %s' % below_block)

    return (left_block, above_block, right_block, below_block)


def findNextPosition(old, layout, robot):
    index = (int((old[0] - 16) / 32), int((old[1] - 16) / 32))

    # environment = ('left', 'above', 'right', 'below')   # always check
    # environment = ('b', 'b', 'b', 'w')
    environment = checkEnvironment(old, layout, robot)        # returns stuff of line above
    current_direction = robot.DIRECTION
    left_is_free = environment[0] == 'w'
    above_is_free = environment[1] == 'w'
    right_is_free = environment[2] == 'w'
    below_is_free = environment[3] == 'w'


    if current_direction == 'below':
        print('BELOW IS FREE: ', below_is_free)
        if below_is_free:
            robot.DIRECTION = 'below'
            return (old[0], old[1] + 32)
        elif left_is_free:
            robot.DIRECTION = 'left'
            return (old[0] - 32, old[1])
        elif above_is_free:
            robot.DIRECTION = 'above'
            return (old[0], old[1] - 32)
        else:
            robot.DIRECTION = 'right'
            return (old[0] + 32, old[1])
    elif current_direction == 'right':
        print('RIGHT IS FREE: ', right_is_free)
        if right_is_free:
            robot.DIRECTION = 'right'
            return (old[0] + 32, old[1])
        elif below_is_free:
            robot.DIRECTION = 'below'
            return (old[0], old[1] + 32)
        elif above_is_free:
            robot.DIRECTION = 'above'
            return (old[0], old[1] - 32)
        elif left_is_free:
            robot.DIRECTION = 'left'
            return (old[0] - 32, old[1])
        
    elif current_direction == 'left':
        print('LEFT IS FREE: ', left_is_free)
        if left_is_free:
            robot.DIRECTION = 'left'
            return (old[0] - 32, old[1])
        elif below_is_free:
            robot.DIRECTION = 'below'
            return (old[0], old[1] + 32)
        elif above_is_free:
            robot.DIRECTION = 'above'
            return (old[0], old[1] - 32)
        elif right_is_free:
            robot.DIRECTION = 'right'
            return (old[0] + 32, old[1])
    elif current_direction == 'above':
        print('ABOVE IS FREE: ', above_is_free)
        if above_is_free:
            robot.DIRECTION = 'above'
            return (old[0], old[1] - 32)
        elif right_is_free:
            robot.DIRECTION = 'right'
            return (old[0] + 32, old[1])
        elif left_is_free:
            robot.DIRECTION = 'left'
            return (old[0] - 32, old[1])
        else:
            robot.DIRECTION = 'below'
            return (old[0], old[1] + 32)
            

    return index



def startLoop():
    path_to_maze = '../examples/maze3.csv'
    new_maze = createMaze()
    maze_layout = loadMaze(new_maze, path_to_maze)
    new_maze.drawMaze(maze_layout)
    starting_point = findStartingPoint(maze_layout)
    robot = createRobot(starting_point)
    robot.drawRobot()
    last_position = starting_point
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        next_position = findNextPosition(last_position, maze_layout, robot)
        time.sleep(1)
        last_position = next_position
        robot.move(next_position)

        # screen.fill(black)
        pygame.display.flip()


startLoop()