import math
import pygame
from Bullet import *

class bulletLauncher:
    def __init__(self, 
    isAuto:bool, 
    fireRate:int,
    damage:int, 
    speed:int, 
    size:int, 
    range:int, 
    tracerColor: tuple[int,int,int]):
        self.isAuto = isAuto
        self.fireRate = fireRate
        self.fireDelay = 0
        self.missleDamage = damage
        self.missleSpeed = speed
        self.missleSize = size
        self.tracer = tracerColor
        self.range = range
    
    def fire(self, game_instance, owner):
        if self.fireDelay == 0:
            x,y = pygame.mouse.get_pos()
            self.spawnBullet(game_instance, owner, math.atan2((y-250),(x-250)), owner.hitbox.center)
            self.fireDelay = self.fireRate

    def spawnBullet(self, game_instance, owner,angle, spaawncoords: tuple[int,int], damageMultiplier = 1):
        Bullet(game_instance, owner, angle,self.range, spaawncoords)