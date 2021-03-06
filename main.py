import pygame
import random


class Ball:
    def __init__(self, pos):
        self.pos = pos
        self.right = True
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(0, 200))
        self.stop = False
        self.speed = random.randint(1, 3)
        pygame.draw.circle(screen, self.color, self.pos, 50)

    def hmove(self):
        if self.pos[0] >= 550:
            self.right = False
        if self.pos[0] <= 50:
            self.right = True
        if self.right:
            self.pos = (self.pos[0] + self.speed, self.pos[1])
        else:
            self.pos = (self.pos[0] - self.speed, self.pos[1])

    def redraw(self):
        pygame.draw.circle(screen, self.color, self.pos, 50)


pygame.init()

screen = pygame.display.set_mode((600, 300))
running = True
FPS = 150
clock = pygame.time.Clock()
circle_color = (236, 176, 199)
balls = list()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = event.pos
                ball = Ball(pos)
                balls.append(ball)
            else:
                if balls:
                    del balls[0]
    for ball in balls:
        ball.hmove()
        ball.redraw()
    pygame.display.flip()
    screen.fill((112, 146, 190))
    clock.tick(FPS)
pygame.quit()
