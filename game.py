import pygame
from settings import *
from models import Grid

class MinesweeperGame:
    def __init__(self, rows, cols, num_mines):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.grid = Grid(rows, cols, num_mines)
        
        self.state = "PLAYING" 
        self.timer_started = False

    def reveal_all_cells(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.grid.grid[row][col]
                cell.reveal()
                if cell.is_mine:
                    cell.exploded = True

    def check_victory(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.grid.grid[row][col]
                if not cell.is_mine and not cell.is_revealed:
                    return False
        return True

    def handle_click(self, pos, button):
        if self.state != "PLAYING":
            return

        col, row = pos[0] // TILE_SIZE, pos[1] // TILE_SIZE
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return

        cell = self.grid.grid[row][col]

        if button == 1:  # Botão Esquerdo
            self.grid.reveal_cell(row, col)
            if cell.is_mine:
                self.reveal_all_cells()
                self.state = "GAME_OVER"
                pygame.time.set_timer(pygame.USEREVENT, 1000) # 1 segundo para ir pra tela de derrota
            elif self.check_victory():
                self.state = "VICTORY"
                pygame.time.set_timer(pygame.USEREVENT, 1000)

        elif button == 3:  # Botão Direito
            cell.toggle_flag()

    def draw(self, surface, assets):
        surface.fill(WHITE)
        self.grid.draw(surface, assets)