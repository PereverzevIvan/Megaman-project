from pygame import Surface
from pygame.image import load
from pygame.sprite import Sprite, collide_rect, spritecollide
from Settings import *
from Bullet import Bullet

class Mob(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((25, 60))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = 25
        self.height = 60
        self.hp = 50

    def collide_detect(self):
        if spritecollide(self, BULLETS, True):
            self.hp -= BULLET_DAMAGE

    def update(self):
        self.collide_detect()
        if self.hp <= 0:
            self.kill()

