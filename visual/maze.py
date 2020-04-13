import sys, pygame

pygame.init()
size = width, height = 512, 512
speed = [2, 0]                              # one has to be zero in order for it to move: left, right, top, down
black = 0, 0, 0
screen = pygame.display.set_mode(size)


def drawMaze():
    pass


def startGameLoop():
    # mouse = pygame.draw.rect(screen, (0,255,0), )
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
        # screen.blit(screen, mouse)
        pygame.display.flip()


startGameLoop()