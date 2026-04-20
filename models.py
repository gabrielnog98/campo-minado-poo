import pygame
import random
from settings import *

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.is_mine = False
        self.is_revealed = False
        self.neighbor_mines = 0
        self.has_flag = False
        self.exploded = False

    def reveal(self):
        self.is_revealed = True

    def toggle_flag(self):
        if not self.is_revealed:
            self.has_flag = not self.has_flag

    def is_empty(self):
        return not self.is_mine and self.neighbor_mines == 0

    def draw(self, surface, assets):
        x = self.col * TILE_SIZE
        y = self.row * TILE_SIZE
        rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

        if self.is_revealed:
            if self.is_mine:
                img_key = 'explosao' if self.exploded else 'bomba'
                if img_key in assets.images:
                    surface.blit(assets.images[img_key], (x, y))
            else:
                pygame.draw.rect(surface, LIGHT_GRAY, rect)
                if self.neighbor_mines > 0:
                    color = assets.get_number_color(self.neighbor_mines)
                    text = assets.fonts['numbers'].render(str(self.neighbor_mines), True, color)
                    surface.blit(text, (x + TILE_SIZE // 3, y + TILE_SIZE // 4))
        else:
            if self.has_flag:
                if 'flag' in assets.images:
                    surface.blit(assets.images['flag'], (x, y))
            else:
                pygame.draw.rect(surface, GRAY, rect)
        
        pygame.draw.rect(surface, BLACK, rect, 1)


class Grid:
    def __init__(self, rows, cols, num_mines):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.grid = [[Cell(row, col) for col in range(cols)] for row in range(rows)]
        
        self._place_mines()
        self._count_mines()

    def _place_mines(self):
        count = 0
        while count < self.num_mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if not self.grid[row][col].is_mine:
                self.grid[row][col].is_mine = True
                count += 1

    def _count_mines(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col].is_mine:
                    continue
                count = 0
                for i in range(max(0, row - 1), min(self.rows, row + 2)):
                    for j in range(max(0, col - 1), min(self.cols, col + 2)):
                        if self.grid[i][j].is_mine:
                            count += 1
                self.grid[row][col].neighbor_mines = count

    def reveal_cell(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return
            
        cell = self.grid[row][col]
        if cell.is_revealed or cell.has_flag:
            return

        cell.reveal()
        if cell.is_empty():
            for i in range(max(0, row - 1), min(self.rows, row + 2)):
                for j in range(max(0, col - 1), min(self.cols, col + 2)):
                    self.reveal_cell(i, j)

    def draw(self, surface, assets):
        for row in range(self.rows):
            for col in range(self.cols):
                self.grid[row][col].draw(surface, assets)