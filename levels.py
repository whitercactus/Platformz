from constants import *
from player import Player
from lava import Lava
from enemy import Enemy
from platforms import *


class Level(object):
    def __init__(self, player, lava, enemy):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.lava_list = pygame.sprite.Group()
        self.enemy = enemy
        self.enemy_list.add(enemy)
        self.player = player
        self.lava = lava
        self.lava_list.add(self.lava)
        # Background image
        self.background = None

        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -1000

    # Update everythign on this level
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()
        self.lava_list.update()

    def draw(self, screen):
        # Draw the background
        screen.fill(BLUE)
        screen.blit(self.background, (self.world_shift, 0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.lava_list.draw(screen)

    def shift_world(self, shift_x):
        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
        for lava in self.lava_list:
            self.lava.rect.x += shift_x


class Level_01(Level):
    def __init__(self, player, lava, enemy):
        # Call the parent constructor
        Level.__init__(self, player, lava, enemy)

        self.level_limit = -1500
        # Array with width, height, x, and y of platform
        level = [[210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 ]
        self.background = pygame.image.load("background_01.png").convert()
        self.background = pygame.transform.scale(self.background, (2800, 600))
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
            screen.blit(block.image, (block.rect.x, block.rect.y))

        # Add a custom moving platform
        block = MovingPlatform(70, 40)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        self.lava = lava
        self.lava_list.add(self.lava)
        self.spike_list = pygame.sprite.Group()


# Create platforms for the level
class Level_02(Level):
    def __init__(self, player, lava, enemy):
        # Call the parent constructor
        Level.__init__(self, player, lava, enemy)

        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        level = [[210, 70, 500, 550],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1120, 280],
                 ]
        self.background = pygame.image.load("background_02.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (2800, 600))
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.lava = Lava(1000, 500, 20)
        self.platform_list.add(block)
        self.lava = lava
        self.lava_list.add(self.lava)
        self.spike_list = pygame.sprite.Group()


class Level_03(Level):
    def __init__(self, player, lava, enemy):
        # Call the parent constructor
        Level.__init__(self, player, lava, enemy)

        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        level = [[210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 500],
                 [210, 70, 1500, 100],
                 ]
        self.background = pygame.image.load("background_04.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (2800, 600))
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = MovingPlatform(70, 70)
        block.rect.x = 1300
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.lava = Lava(1000, 500, 20)
        self.platform_list.add(block)
        self.lava = lava
        self.lava_list.add(self.lava)
        self.spike_list = pygame.sprite.Group()


class Level_04(Level):
    def __init__(self, player, lava, enemy):
        # Call the parent constructor
        Level.__init__(self, player, lava, enemy)

        self.level_limit = -1500

        # Array with type of platform, and x, y location of the platform.
        level = [[210, 70, 500, 550],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 300],
                 [210, 70, 1120, 480],
                 ]
        self.background = pygame.image.load("background_03.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (2800, 600))
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block1 = MovingPlatform(70, 70)
        block1.rect.x = 1500
        block1.rect.y = 300
        block1.boundary_top = 100
        block1.boundary_bottom = 550
        block1.change_y = -1
        block1.player = self.player
        block1.level = self
        self.lava = Lava(1000, 500, 20)
        self.platform_list.add(block1)
        self.lava = lava
        self.lava_list.add(self.lava)
        self.spike_list = pygame.sprite.Group()


class Level_05(Level):
    def __init__(self, player, lava, enemy):
        # Call the parent constructor
        Level.__init__(self, player, lava, enemy)

        self.level_limit = -1500

        # Array with width, height, x, and y of platform
        level = [[210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 300],
                 [210, 70, 1120, 280],
                 ]

        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
        self.background = pygame.image.load("background_05.png").convert()
        self.background = pygame.transform.scale(self.background,(2800,600))
        # Add a custom moving platform
        block = MovingPlatform(70, 40)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        block1 = MovingPlatform(70, 70)
        block1.rect.x = 1500
        block1.rect.y = 300
        block1.boundary_top = 100
        block1.boundary_bottom = 550
        block1.change_y = -1
        block1.player = self.player
        block1.level = self
        self.lava = Lava(1000, 500, 20)
        self.platform_list.add(block1)
        self.lava = lava
        self.lava_list.add(self.lava)
        self.spike_list = pygame.sprite.Group()


class Level_06(Level):
    def __init__(self, player, lava, enemy):
        Level.__init__(self, player, lava, enemy)
        self.level_limit = - 2000

        level = [[210, 70, 500, 500],
                 [210, 70, 800, 400],
                 [210, 70, 1000, 280],
                 [210, 70, 1120, 180],
                 [210, 70, 1300, 300],
                 [210, 70, 1500, 200],
                 [210, 70, 1800, 100],
                 [210, 70, 2000, 200]
                 ]
        self.background = pygame.image.load("background.png").convert()
        self.background = pygame.transform.scale(self.background,(3300,600))
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        block = MovingPlatform(70, 100)
        block.rect.x = 2200
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.lava = Lava(1000, 500, 20)
        self.platform_list.add(block)
        self.lava = lava
        self.lava_list.add(self.lava)
        self.spike_list = pygame.sprite.Group()

