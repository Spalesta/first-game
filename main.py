import pygame
import random


class Ball:
    def __init__(self, pos):
        self.radius = random.randint(20, 40)
        self.pos = pos
        self.right = True
        self.up = True
        self.color = (random.randint(100, 255), random.randint(100, 255), random.randint(0, 200))
        self.stop = False
        self.xspeed = random.randint(-7, 7)
        self.yspeed = random.randint(-7, 7)
        if self.xspeed == 0 and self.yspeed == 0:
            self.xspeed, self.yspeed = random.randint(1, 7), random.randint(1, 7)
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

    def ymove(self):
        if self.pos[1] >= y_limit - self.radius or self.pos[1] <= self.radius:
            self.yspeed = -self.yspeed
        self.pos = (self.pos[0], self.pos[1] + self.yspeed)

    def xmove(self):
        if self.pos[0] >= x_limit - self.radius or self.pos[0] <= self.radius:
            self.xspeed = -self.xspeed
        self.pos = (self.pos[0] + self.xspeed, self.pos[1])

    def redraw(self):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

    def delete(self, other):
        if (self.pos[0] - other.pos[0]) ** 2 + (self.pos[1] - other.pos[1]) ** 2 <= (self.radius + other.radius) ** 2:
            return True


pygame.init()

radius = 45
y_limit = 500
x_limit = 800
screen = pygame.display.set_mode((x_limit, y_limit))
running = True
FPS = 80
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
                if pos[0] <= radius:
                    pos = (radius + 1, pos[1])
                elif pos[0] >= x_limit - radius:
                    pos = (x_limit - radius - 1, pos[1])
                if pos[1] <= radius:
                    pos = (pos[0], radius + 1)
                elif pos[1] >= y_limit - radius:
                    pos = (pos[0], y_limit - radius - 1)
                ball = Ball(pos)
                balls.append(ball)
            else:
                if balls:
                    del balls[0]
    i = 0
    while i < len(balls):
        j = i + 1
        while j < len(balls):
            if balls[i].delete(balls[j]):
                balls.pop(j)
                balls.pop(i)
                break
            else:
                j += 1
        i += 1

    for ball in balls:
        ball.xmove()
        ball.ymove()
        ball.redraw()
    pygame.display.flip()
    screen.fill((180, 222, 250))
    clock.tick(FPS)
pygame.quit()
