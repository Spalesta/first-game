import pygame
x, y = 600, 300
screen = pygame.display.set_mode((x, y))
screen_color = (0, 0, 0)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cell_size = 30
        self.matrix = [[0] * (self.height // self.cell_size) for _ in range(self.width // self.cell_size)]

    def redraw(self):
        x, y = 0, 0
        for i in range(self.height // self.cell_size):
            for j in range(self.width // self.cell_size):
                if not self.matrix[i][j]:
                    pygame.draw.rect(screen, (200, 200, 200), (i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size), 1)
                else:
                    pygame.draw.rect(screen, (200, 200, 200),(i * self.cell_size, j * self.cell_size, self.cell_size, self.cell_size))

    def paint(self, pos):
        x, y = pos
        self.matrix[pos[0] // self.cell_size][pos[1] // self.cell_size] = 1

    def not_paint(self, pos):
        x, y = pos
        self.matrix[pos[0] // self.cell_size][pos[1] // self.cell_size] = 0


board = Board(1000, 1000)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = event.pos
                board.paint(pos)
            elif event.button == 3:
                pos = event.pos
                board.not_paint(pos)
    screen.fill(screen_color)
    board.redraw()


    pygame.display.flip()