from pygame.sprite import Group
from pygame.image import load
import os

# Total
SIZE = (1280, 720)
FPS = 60

# for Megaman
MEGAMAN_SPEED = 0.3
GRAVITY_POWER = 0.7
SLIDING_ON_GROUND = 0.7
SLIDING_ON_ICE = 0.2
JUMP_POWER = 14
WALK_RIGHT_ANIM = [load(f'Megaman sprites/megaman walk right {i}.png') for i in [2, 3, 2, 4]]
WALK_LEFT_ANIM = [load(f'Megaman sprites/megaman walk left {i}.png') for i in [2, 3, 2, 4]]
STAND_RIGHT_ANIM = [load('Megaman sprites/megaman standing right.png'), load('Megaman sprites/megaman blink right.png')]
STAND_LEFT_ANIM = [load('Megaman sprites/megaman standing left.png'), load('Megaman sprites/megaman blink left.png')]
JUMP_LEFT = load('Megaman sprites/Megaman jump left.png')
JUMP_RIGHT = load('Megaman sprites/Megaman jump right.png')
STAND_AND_SHOT_R = load('Megaman sprites/megaman shot right.png')
STAND_AND_SHOT_L = load('Megaman sprites/megaman shot left.png')

# for bullets
BULLET_SPEED = 15
BULLET_DAMAGE = 10

# for all
BULLETS = Group()
MOBS = Group()
PLATFORMS = Group()
ALL_SPRITES = Group()

TOTAL_LEVEL_WIDTH = 0
TOTAL_LEVEL_HEIGHT = 0
