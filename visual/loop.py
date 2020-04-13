import sys, pygame
from maze import Maze as mz

pygame.init()
size = width, height = 512, 512
maze_size = { 'x': 512, 'y': 512 }
speed = [2, 0]                              # one has to be zero in order for it to move: left, right, top, down
black = 0, 0, 0
screen = pygame.display.set_mode(size)


def drawMaze():
    da_maze = mz(maze_size, { 'x': 64, 'y': 64 }, { 'x': 8, 'y': 8})
    da_maze.loadMaze('examples/maze.csv')


def startGameLoop():
    drawMaze()
    mouse = pygame.Rect((0,0), (64, 64))
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()


        mouse = mouse.move(speed)
        if mouse.left < 0 or mouse.right > width:
            speed[0] = -speed[0]
        if mouse.top < 0 or mouse.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        pygame.draw.rect(screen, (0,255,0), mouse)
        pygame.display.flip()


startGameLoop()