import sys, pygame
from maze import Maze as mz
from robot import Robot as robo
from solver import Solver as solve
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


def startLoop():
    path_to_maze = '../examples/maze4.csv'
    new_maze = createMaze()
    maze_layout = loadMaze(new_maze, path_to_maze)
    new_maze.drawMaze(maze_layout)

    maze_solver = solve(maze_layout)    # JUST for init
    starting_point = maze_solver.findStartingPoint(maze_layout)
    ending_point = maze_solver.findEndingPoint(maze_layout)
    last_position = starting_point
    visited = []

    maze_solver = solve(maze_layout, starting_point, last_position, last_position, visited)
    
    robot = createRobot(maze_solver.START)
    robot.drawRobot()
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        if (maze_solver.CURRENT != ending_point):
            visited.append(maze_solver.LAST)
            next_position = maze_solver.findNextPosition(maze_solver.CURRENT, maze_layout, robot, visited)
            time.sleep(0.5)
            last_position = maze_solver.CURRENT
            maze_solver.LAST = last_position
            robot.move(maze_solver.LAST, next_position)

            maze_solver.CURRENT = next_position

        elif (maze_solver.CURRENT == ending_point):
            screen.fill(black)
            myfont = pygame.font.SysFont("Comic Sans MS", 30)
            label = myfont.render("YOU WON!", 1, (240, 255, 0))
            screen.blit(label, (256, 256))
            pygame.display.flip()
            time.sleep(3)
            break


        # screen.fill(black)
        pygame.display.flip()
    


startLoop()