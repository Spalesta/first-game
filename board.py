# -*- coding: utf-8 -*-
import pygame
import random
x, y = 600, 300
screen = pygame.display.set_mode((x, y))
screen_color = (0, 0, 0)


class Board:
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.cell_size = 30
        self.cells_height = self.height // self.cell_size  # количество клеток в высоту
        self.cells_width = self.width // self.cell_size  # количество клеток в ширину

        self.matrix = [[False] * self.cells_width for _ in range(self.cells_height)]
        print(self.cells_height, self.cells_width)
        print(self.matrix)

    def redraw(self):
        for i in range(self.cells_height):
            for j in range(self.cells_width):
                if not self.matrix[i][j]:  # если в ячейке матрицы False:
                    pygame.draw.rect(screen, (200, 200, 200), (i * self.cell_size, j * self.cell_size, self.cell_size,
                                                               self.cell_size), 1)  # незакрашенный
                else:
                    pygame.draw.rect(screen, (200, 200, 200), (i * self.cell_size, j * self.cell_size, self.cell_size,
                                                               self.cell_size))  # закрашенный

    def click(self, pos):
        x, y = pos
        self.matrix[x // self.cell_size][y // self.cell_size] = not(self.matrix[x // self.cell_size][y // self.cell_size])

    def fill_random_cells(self):
        for _ in range(3):
            y = random.randint(0, len(self.matrix))
            while all(self.matrix[y]):
                y = random.randint(0, len(self.matrix))
            x = random.randint(0, len(self.matrix[0]))
            while self.matrix[x][y]:
                x = random.randint(0, len(self.matrix))
            self.matrix[x][y] = True



board = Board(x, y)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = event.pos
                board.click(pos)

    screen.fill(screen_color)
    board.redraw()

    pygame.display.flip()
