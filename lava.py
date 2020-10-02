from constants import *


class Lava(pygame.sprite.Sprite):
    def __init__(self, width, x, y):
        super().__init__()
        self.image = pygame.image.load("lava.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, 50))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.change = 0
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x -= self.change