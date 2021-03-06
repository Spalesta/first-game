import pygame

class Ball():
    def __init__(self, pos, color):
        self.pos = pos
        self.right = True
        self.color = color
        self.stop = False
        pygame.draw.circle(screen, self.color, self.pos, 50)
    def move(self):
        self.pos = (self.pos[0] + 1, self.pos[1])
        if not self.stop:
            if self.pos[0] == 550:
                self.right = False
            if self.pos[0] == 50:
                self.right = True
            if self.right:
                self.pos = (self.pos[0], self.pos[1])
            else:
                self.pos = (self.pos[0], self.pos[1])
    def redraw(self):
        pygame.draw.circle(screen, self.color, self.pos, 50)


pygame.init()

screen = pygame.display.set_mode((600, 300))
screen.fill((112, 146, 190))
x, y = 100, 100
right = True
running = True
FPS = 200
clock = pygame.time.Clock()
circle_color = (236, 176, 199)
screen_color = (112, 146, 190)
stop = False
ball = Ball((x, y), circle_color)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                stop = True
            else:
                stop = False
        '''if event.type == pygame.MOUSEBUTTONUP:
            stop = False'''
    pygame.display.flip()
    screen.fill((112, 146, 190))

    ball.redraw()

    ball.move()
    ball.redraw()
    clock.tick(FPS)

pygame.quit()
