import pygame as pg
from Settings import *
from Megaman import Megaman
from Create_levels import level_one, create_level
from Camera import Camera


def camera_func(camera, target):
    camera_x = -target.rect.x + SIZE[0] / 2
    camera_y = -target.rect.y + SIZE[1] / 2
    w, h = camera.width, camera.height
    camera_x = min(0, camera_x)
    camera_x = max(-(w - SIZE[0]), camera_x)
    camera_y = max(-(h - SIZE[1]), camera_y)
    camera_y = min(0, camera_y)
    return pg.Rect(int(camera_x), int(camera_y), w, h)


def health_bar_update(megaman):
    x = 20
    y = 167
    for i in range(megaman.hp):
        if i % 2 == 0:
            pg.draw.rect(screen, (255, 255, 0), (x, y, 20, 3))
        else:
            pg.draw.rect(screen, (155, 155, 0), (x, y, 20, 3))
        y -= 2


pg.init()

pg.display.set_caption('Megaman')
window = pg.display.set_mode(SIZE)
screen = pg.Surface(SIZE, pg.SRCALPHA)
clock = pg.time.Clock()

GAME_OVER = False
megaman = Megaman(100, 40)
create_level(level_one)
right = left = up = False

camera = Camera(camera_func, TOTAL_LEVEL_WIDTH, TOTAL_LEVEL_HEIGHT)

while not GAME_OVER:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            GAME_OVER = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_x:
                megaman.get_hp(10)
            if event.key == pg.K_c:
                megaman.get_damage(10)
            if event.key == pg.K_UP:
                megaman.shoot()
            if event.key == pg.K_RIGHT:
                right = True
                left = False
            elif event.key == pg.K_LEFT:
                left = True
                right = False
            elif event.key == pg.K_SPACE:
                if up:
                    up = False
                else:
                    up = True
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT:
                right = False
            elif event.key == pg.K_LEFT:
                left = False
            elif event.key == pg.K_SPACE:
                up = False

    screen.fill((0, 0, 0, 0))
    window.fill((100, 142, 255))

    megaman.update(right, left, up)
    PLATFORMS.update()
    BULLETS.update()
    MOBS.update()
    PLATFORMS.draw(screen)
    BULLETS.draw(screen)
    MOBS.draw(screen)
    screen.blit(megaman.image, megaman.get_coords_for_rect())
    pg.draw.rect(screen, (0, 0, 0), (20, 20, 20, 150))
    pg.draw.rect(screen, (255, 0, 0), (megaman.rect.x, megaman.rect.y, megaman.rect.width, megaman.rect.height),
                 width=1)
    health_bar_update(megaman)

    window.blit(screen, (0, 0))

    pg.display.flip()
    clock.tick(FPS)
