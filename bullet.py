from constants import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change = 7
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self):
        self.rect.x += self.change

