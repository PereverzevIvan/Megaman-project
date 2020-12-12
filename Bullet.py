from pygame import Surface
from pygame.sprite import Sprite, spritecollide
from Settings import *


class Bullet(Sprite):
    def __init__(self, x, y, nap):
        Sprite.__init__(self)
        self.image = Surface((10, 10))
        self.rect = self.image.get_rect()
        if nap == 'right':
            self.speed = BULLET_SPEED
            self.rect.x, self.rect.y = x + 52, y + 17
        elif nap == 'left':
            self.speed = -BULLET_SPEED
            self.rect.x, self.rect.y = x - 15, y + 17
        self.image.fill((255, 255, 0))

    def collide_detect(self):
        if spritecollide(self, MOBS, False):
            self.kill()

    def update(self):
        self.rect.x += self.speed
        # self.collide_detect()  # Пока не используется
        if self.rect.x > SIZE[0] or self.rect.x < 0:
            self.kill()
