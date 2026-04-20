import pygame
import sys
from settings import *
from assets import AssetManager
from screens import Screens
from game import MinesweeperGame

class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Campo Minado")
        
        self.rows = DEFAULT_ROWS
        self.cols = DEFAULT_COLS
        self.num_mines = DEFAULT_NUM_MINES
        
        self.state = "MENU"
        
        self.update_display()
        self.assets = AssetManager(TILE_SIZE)
        self.game = None
        self.clock = pygame.time.Clock()

    def update_display(self):
        # Atualiza o tamanho da janela com base nas linhas/colunas
        self.width = self.cols * TILE_SIZE
        self.height = self.rows * TILE_SIZE
        self.screen = pygame.display.set_mode((self.width, self.height))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT:
                pygame.time.set_timer(pygame.USEREVENT, 0) # Para o timer
                if self.game.state == "GAME_OVER":
                    self.state = "GAME_OVER_SCREEN"
                elif self.game.state == "VICTORY":
                    self.state = "VICTORY_SCREEN"

            if event.type == pygame.KEYDOWN:
                self.handle_keydown(event)

            if event.type == pygame.MOUSEBUTTONDOWN and self.state == "PLAYING":
                self.game.handle_click(event.pos, event.button)

    def handle_keydown(self, event):
        if self.state == "MENU":
            if event.key == pygame.K_RETURN:
                self.state = "SETTINGS"
                
        elif self.state == "SETTINGS":
            if event.key == pygame.K_w:
                self.rows = min(self.rows + 1, 20)
            elif event.key == pygame.K_s:
                self.rows = max(self.rows - 1, 5)
            elif event.key == pygame.K_d:
                self.cols = min(self.cols + 1, 20)
            elif event.key == pygame.K_a:
                self.cols = max(self.cols - 1, 5)
            elif event.key in (pygame.K_PLUS, pygame.K_EQUALS, pygame.K_KP_PLUS):
                self.num_mines = min(self.num_mines + 5, self.rows * self.cols - 1)
            elif event.key in (pygame.K_MINUS, pygame.K_KP_MINUS):
                self.num_mines = max(self.num_mines - 5, 5)
            elif event.key == pygame.K_RETURN:
                self.update_display()
                self.game = MinesweeperGame(self.rows, self.cols, self.num_mines)
                self.state = "PLAYING"

        elif self.state in ("GAME_OVER_SCREEN", "VICTORY_SCREEN"):
            if event.key == pygame.K_RETURN:
                self.state = "SETTINGS"
                self.rows, self.cols = DEFAULT_ROWS, DEFAULT_COLS
                self.update_display()

    def draw(self):
        if self.state == "MENU":
            Screens.draw_main_menu(self.screen, self.assets, self.width, self.height)
        elif self.state == "SETTINGS":
            Screens.draw_settings_menu(self.screen, self.assets, self.width, self.height, 
                                       self.rows, self.cols, self.num_mines)
        elif self.state == "PLAYING":
            self.game.draw(self.screen, self.assets)
        elif self.state == "GAME_OVER_SCREEN":
            Screens.draw_game_over_screen(self.screen, self.assets, self.width, self.height)
        elif self.state == "VICTORY_SCREEN":
            Screens.draw_victory_screen(self.screen, self.assets, self.width, self.height)

        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.draw()
            self.clock.tick(60)

if __name__ == "__main__":
    app = App()
    app.run()