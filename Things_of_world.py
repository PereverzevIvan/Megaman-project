from pygame import Surface
from pygame.sprite import Sprite
from pygame.image import load
from pygame import transform


class CommonBlock(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('Окружение/Cut man stage/Common block.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.width = 80
        self.height = 80

    def update(self):
        pass


class LowBlock(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = Surface((80, 40))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.width = 80
        self.height = 40
        self.image.fill((100, 42, 42))

    def update(self):
        pass
