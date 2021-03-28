# -*- coding: utf-8 -*-
import pygame
import random
import time
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
            y = random.randint(0, len(self.matrix) - 1)
            if all(self.matrix[y]):
                y = random.randint(0, len(self.matrix) - 1)
            x = random.randint(0, len(self.matrix[0]) - 1)
            if self.matrix[y][x]:
                x = random.randint(0, len(self.matrix[0]) - 1)
            self.matrix[y][x] = not self.matrix[y][x]


board = Board(x - 30, y - 30)
last_time = time.time()
start_time = last_time
time_to_fuck_things_up = 3

running = True
while running:
    current_time = int(time.time() - last_time)
    if current_time is time_to_fuck_things_up:
        board.fill_random_cells()
        last_time = time.time()
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
