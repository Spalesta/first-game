import pygame
x, y = 600, 300
screen = pygame.display.set_mode((x, y))
screen_color = (0, 0, 0)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cell_size = 30

    def redraw(self):
        x, y = 0, 0
        for i in range(self.height // self.cell_size):
            for j in range(self.width // self.cell_size):
                pygame.draw.rect(screen, (200, 200, 200), (i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size), 1)


board = Board(1000, 1000)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(screen_color)
    board.redraw()


    pygame.display.flip()