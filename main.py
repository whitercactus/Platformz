import pygame
from constants import *
from player import Player
from platforms import *
from lava import Lava
from enemy import Enemy
from bullet import Bullet
from levels import *
pygame.init()


def main():
    pygame.init()
    # Set the height and width of the screen

    pygame.display.set_caption("Platformz")
    pygame.display.set_icon(Player().image)
    shot = False
    font = pygame.font.SysFont("ComicSans", 50)

    # Create the player
    player = Player()
    screen.blit(player.image, (player.rect.x, player.rect.y))
    # Create all the levels
    level_list = []
    level_list.append(Level_01(player, Lava(1450, 500, 575), Enemy(1000, 420)))
    level_list.append(Level_02(player, Lava(1450, 500, 575), Enemy(900, 320)))
    level_list.append(Level_03(player, Lava(1450, 500, 575), Enemy(1500, 20)))
    level_list.append(Level_04(player, Lava(1450, 500, 575), Enemy(1000, 220)))
    level_list.append(Level_05(player, Lava(1450, 500, 575), Enemy(800, 320)))
    level_list.append(Level_06(player, Lava(1900, 500, 575), Enemy(1500, 120)))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    done = False

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player.rect.x + 40, player.rect.y + 30)
                    shot = True
                    active_sprite_list.add(bullet)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        active_sprite_list.update()
        current_level.update()
        current_level.lava_list.draw(screen)

        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            if current_level_no < len(level_list) - 1:
                player.rect.x = 120
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
                player.lava = current_level.lava
            else:
                done = True
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        if shot:
            pygame.sprite.spritecollide(bullet, current_level.enemy_list, True)
        hit = pygame.sprite.spritecollide(player, current_level.enemy_list, False)
        if hit:
            main()
        hitLava = pygame.sprite.spritecollide(player, current_level.lava_list, False)
        if hitLava:
            main()

        clock.tick(60)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
