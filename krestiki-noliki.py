import pygame

pygame.init()


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cell_size = 30
        self.cheight = self.height // self.cell_size
        self.cwidth = self.width // self.cell_size
        self.matrix=[[0] * (self.cheight) for _ in range(self.cwidth)]
        self.crest = True

    def draw(self):
        for i in range(self.cwidth):
            for j in range(self.cheight):
                x = j * self.cell_size
                y = i * self.cell_size
                if self.matrix[i][j] == 0:
                    pygame.draw.rect(screen, (242, 255, 191), (x, y, self.cell_size, self.cell_size), 1)
                elif self.matrix[i][j] == 1:
                    pygame.draw.rect(screen, (242, 255, 191), (x, y, self.cell_size, self.cell_size), 1)
                    pygame.draw.line(screen,(242, 255, 191), (x, y), (x + self.cell_size, y + self.cell_size), 3)
                    pygame.draw.line(screen, (242, 255, 191), (x + self.cell_size, y), (x, y + self.cell_size), 3)
                elif self.matrix[i][j] == 2:
                    pygame.draw.rect(screen, (242, 255, 191), (x, y,  self.cell_size, self.cell_size), 1)
                    pygame.draw.circle(screen, (242, 255, 191), (x + self.cell_size // 2, y + self.cell_size // 2), self.cell_size // 2 - 2, 2)


    def on_click(self, x, y):
        if self.matrix[x // self.cell_size][y // self.cell_size] == 0:
            if self.crest:
                self.matrix[x // self.cell_size][y // self.cell_size] = 1
            else:
                self.matrix[x // self.cell_size][y // self.cell_size] = 2
            self.crest = not self.crest

    '''def check(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 1 or self.matrix[i][j] == 2:
                    if self.matrix[i][j] == 1:
                        if j != 0:
                            if self.matrix[i][j - 1] == 1 and self.matrix[i][j + 1] == 1:
                                pass
                        else:
                            if j == len(self.matrix[i]) - 1:
                                if self.matrix[i][j - 1]'''

x, y = 620, 620
screen = pygame.display.set_mode((x, y))
main_board = Board(y, x)
running = True
while running:
    screen.fill((2, 40, 9))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            main_board.on_click(event.pos[1], event.pos[0])
    main_board.draw()
    pygame.display.flip()