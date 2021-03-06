import pygame


class Ball:
    def __init__(self, pos, color):
        self.pos = pos
        self.right = True
        self.color = color
        self.stop = False
        pygame.draw.circle(screen, self.color, self.pos, 50)

    def hmove(self):
        if self.pos[0] == 550:
            self.right = False
        if self.pos[0] == 50:
            self.right = True
        if self.right:
            self.pos = (self.pos[0] + 1, self.pos[1])
        else:
            self.pos = (self.pos[0] - 1, self.pos[1])

    def redraw(self):
        pygame.draw.circle(screen, self.color, self.pos, 50)


pygame.init()

screen = pygame.display.set_mode((600, 300))
running = True
FPS = 200
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
                ball = Ball(pos, circle_color)
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
