from constants import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.image = pygame.transform.flip(self.image,True,False)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        screen.blit(self.image, (self.rect.x, self.rect.y))

