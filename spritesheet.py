import pygame
class SpriteSheet(object):
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert_alpha()
        image.fill((0,0,0,0))
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return image
