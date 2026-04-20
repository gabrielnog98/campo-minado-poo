import pygame
import os

class AssetManager:
    def __init__(self, tile_size):
        self.tile_size = tile_size
        self.images = {}
        self.fonts = {}
        self._load_images()
        self._load_fonts()

    def _load_images(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        image_dir = os.path.join(base_dir, 'Imagens')

        try:
            flag = pygame.image.load(os.path.join(image_dir, 'flag.png')).convert_alpha()
            bomba = pygame.image.load(os.path.join(image_dir, 'bomba.png')).convert_alpha()
            explosao = pygame.image.load(os.path.join(image_dir, 'explosao.png')).convert_alpha()

            self.images['flag'] = pygame.transform.scale(flag, (self.tile_size, self.tile_size))
            self.images['bomba'] = pygame.transform.scale(bomba, (self.tile_size, self.tile_size))
            self.images['explosao'] = pygame.transform.scale(explosao, (self.tile_size, self.tile_size))
            print(f"Imagens carregadas com sucesso da pasta: {image_dir}") # Aviso no terminal para confirmar!
            
        except FileNotFoundError as e:
            print(f"Erro ao carregar imagens. Verifique se os arquivos estão em: {image_dir}")
            print(f"Detalhe do erro: {e}")

    def _load_fonts(self):
        self.fonts['numbers'] = pygame.font.SysFont(None, 36)
        self.fonts['title'] = pygame.font.SysFont(None, 72)
        self.fonts['menu'] = pygame.font.SysFont(None, 48)
        self.fonts['text'] = pygame.font.SysFont(None, 36)

    def get_number_color(self, number):
        colors = {
            1: (0, 0, 255),       # Azul
            2: (0, 255, 0),       # Verde
            3: (255, 0, 0),       # Vermelho
            4: (0, 0, 139)        # Azul Escuro
        }
        return colors.get(number, (0, 0, 0)) # Preto por padrão