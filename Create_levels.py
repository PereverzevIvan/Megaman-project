from Things_of_world import CommonBlock, LowBlock
from Settings import *
from Mobs import Mob


def create_level(level):
    x = y = 0
    max_x, max_y = 0, 0
    for row in level:
        for thing in row:
            if thing == '1':
                plat = CommonBlock(x, y)
                PLATFORMS.add(plat)
                x += plat.width
            elif thing == ' ':
                x += 80
            elif thing == '2':
                plat = LowBlock(x, y + 40)
                PLATFORMS.add(plat)
                x += plat.width
            elif thing == 'M':
                mob = Mob(x, y + 20)
                MOBS.add(mob)
                x += (80 - mob.width)
        max_x = max(max_x, x)
        y += 80
        x = 0
    max_y = y
    TOTAL_LEVEL_WIDTH = max_x
    TOTAL_LEVEL_HEIGHT = max_y


level_one = [
    '                                    ',
    '                                    ',
    '                                    ',
    '                                    ',
    '                                    ',
    '           M                        ',
    '111       111111                    ',
    ' M    11   M  M                     ',
    '111111111111111111111111111111111111',
]
