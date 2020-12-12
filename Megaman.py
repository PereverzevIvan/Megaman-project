from pygame.sprite import Sprite, collide_rect, spritecollide
from Settings import *
from Bullet import Bullet


class Megaman(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = STAND_RIGHT_ANIM[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.x_vel = self.y_vel = 0
        self.return_impulse = 15

        self.on_ground = False
        self.right = True
        self.left = False
        self.walk = False
        self.in_jump = True
        self.shot = False

        self.anim_count_walk = 0
        self.anim_count_stand = 0
        self.anim_count_shot = 0

        self.hp = 75

    def animation(self):
        if self.walk:
            frame = self.anim_count_walk // 7
            if self.right:
                if self.in_jump:
                    self.image = JUMP_RIGHT
                else:
                    self.image = WALK_RIGHT_ANIM[frame]
            elif self.left:
                if self.in_jump:
                    self.image = JUMP_LEFT
                else:
                    self.image = WALK_LEFT_ANIM[frame]
            self.anim_count_walk = self.anim_count_walk + 1 if self.anim_count_walk < 27 else 0
        else:
            frame = self.anim_count_stand // 180
            if self.right:
                if self.in_jump:
                    self.image = JUMP_RIGHT
                else:
                    if self.shot:
                        self.image = STAND_AND_SHOT_R
                        self.anim_count_shot += 1
                    else:
                        self.image = STAND_RIGHT_ANIM[frame]
            elif self.left:
                if self.in_jump:
                    self.image = JUMP_LEFT
                else:
                    if self.shot:
                        self.image = STAND_AND_SHOT_L
                        self.anim_count_shot += 1
                    else:
                        self.image = STAND_LEFT_ANIM[frame]
            self.anim_count_stand = 0 if self.anim_count_stand > 200 else self.anim_count_stand + 1
            if self.anim_count_shot >= 25:
                self.shot = False
                self.anim_count_shot = 0

    def collides_detect(self, x_vel, y_vel):
        if spritecollide(self, MOBS, False):
            self.rect.x += self.return_impulse if self.x_vel < 0 else -self.return_impulse
            self.x_vel = 0
            self.get_damage(10)
        for p in PLATFORMS:
            if collide_rect(self, p):
                if x_vel > 0:
                    self.rect.right = p.rect.left
                    self.x_vel = 0
                if x_vel < 0:
                    self.rect.left = p.rect.right
                    self.x_vel = 0
                if y_vel > 0:
                    self.rect.bottom = p.rect.top
                    self.on_ground = True
                    self.in_jump = False
                    self.y_vel = 0
                if y_vel < 0:
                    self.rect.top = p.rect.bottom
                    self.y_vel = 0

    def update(self, right, left, up):
        self.animation()
        if right:
            self.walk = True
            self.right = True
            self.left = False
            self.shot = False
            if self.x_vel < 5:
                self.x_vel += MEGAMAN_SPEED
        elif left:
            self.walk = True
            self.left = True
            self.right = False
            self.shot = False
            if self.x_vel > -5:
                self.x_vel += -MEGAMAN_SPEED
        elif not (right or left):
            self.walk = False
            if self.right:
                self.x_vel = self.x_vel - SLIDING_ON_GROUND if self.x_vel > 0 else 0
            if self.left:
                self.x_vel = self.x_vel + SLIDING_ON_GROUND if self.x_vel < 0 else 0
        if up:
            if self.on_ground:
                self.y_vel += -JUMP_POWER
                self.in_jump = True
        if not self.on_ground:
            self.y_vel += GRAVITY_POWER
        self.on_ground = False
        self.rect.x += self.x_vel
        self.collides_detect(self.x_vel, 0)
        self.rect.y += self.y_vel
        self.collides_detect(0, self.y_vel)

    def shoot(self):
        if len(BULLETS) < 3:
            self.shot = True
            self.anim_count_shot = 0
            if self.right:
                bullet = Bullet(self.rect.x, self.rect.y, 'right')
                BULLETS.add(bullet)
            elif self.left:
                bullet = Bullet(self.rect.x, self.rect.y, 'left')
                BULLETS.add(bullet)

    def get_hp(self, value):
        if self.hp < 75:
            self.hp += value
        self.hp = 75 if self.hp > 75 else self.hp

    def get_damage(self, value):
        if self.hp > 0:
            self.hp -= value
        self.hp = 0 if self.hp < 0 else self.hp

    def get_coords_for_rect(self):
        rect = self.image.get_rect(x=self.rect.x, y=self.rect.y)
        x = abs(self.rect.centerx - rect.centerx)
        return self.rect.x - x, self.rect.y
