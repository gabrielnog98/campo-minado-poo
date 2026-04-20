import pygame
from settings import *

class Screens:
    @staticmethod
    def draw_main_menu(surface, assets, width, height):
        surface.fill(WHITE)
        title_text = assets.fonts['title'].render("Campo Minado", True, BLACK)
        title_rect = title_text.get_rect(center=(width // 2, height // 2 - 100))
        surface.blit(title_text, title_rect)

        play_text = assets.fonts['text'].render("Pressione Enter para jogar", True, BLACK)
        play_rect = play_text.get_rect(center=(width // 2, height // 2 + 50))
        surface.blit(play_text, play_rect)

    @staticmethod
    def draw_settings_menu(surface, assets, width, height, rows, cols, mines):
        surface.fill(WHITE)
        title_text = assets.fonts['menu'].render("Configurações", True, BLACK)
        surface.blit(title_text, title_text.get_rect(center=(width // 2, height // 2 - 150)))

        controls = [
            f"Linhas (W/S): {rows}",
            f"Colunas (A/D): {cols}",
            f"Bombas (+/-): {mines}"
        ]

        for i, text in enumerate(controls):
            rendered_text = assets.fonts['text'].render(text, True, BLACK)
            rect = rendered_text.get_rect(center=(width // 2, (height // 2 - 50) + (i * 50)))
            surface.blit(rendered_text, rect)

        start_text = assets.fonts['text'].render("Pressione Enter para começar", True, BLACK)
        surface.blit(start_text, start_text.get_rect(center=(width // 2, height // 2 + 150)))

    @staticmethod
    def draw_victory_screen(surface, assets, width, height):
        surface.fill(WHITE)
        victory_text = assets.fonts['title'].render("Você Venceu!", True, GREEN)
        surface.blit(victory_text, victory_text.get_rect(center=(width // 2, height // 2 - 100)))

        restart_text = assets.fonts['text'].render("Pressione Enter para reiniciar", True, BLACK)
        surface.blit(restart_text, restart_text.get_rect(center=(width // 2, height // 2 + 50)))

    @staticmethod
    def draw_game_over_screen(surface, assets, width, height):
        surface.fill(WHITE)
        game_over_text = assets.fonts['title'].render("Game Over", True, RED)
        surface.blit(game_over_text, game_over_text.get_rect(center=(width // 2, height // 2 - 100)))

        restart_text = assets.fonts['text'].render("Pressione Enter para reiniciar", True, BLACK)
        surface.blit(restart_text, restart_text.get_rect(center=(width // 2, height // 2 + 50)))