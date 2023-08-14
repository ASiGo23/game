import math
import pygame
from Bullet import *

class Weapon:
    def __init__(self,
    isAuto:bool, 
    fireRate:int,
    damage:int, 
    speed:int, 
    size:int, 
    range:int, 
    tracerColor: tuple[int,int,int]):
    
        #self.owner is set by the owner after creation
        self.owner = None
        self.isAuto = isAuto
        self.fireRate = fireRate
        self.fireDelay = 0
        self.missleDamage = damage
        self.missleSpeed = speed
        self.missleSize = size
        self.tracer = tracerColor
        self.range = range
    
    def fire(self):
        if self.fireDelay == 0:
            self.spawnBullet(self.owner, self.owner.aim, self.owner.hitbox.center)
            self.fireDelay = self.fireRate

    def spawnBullet(self, owner, angle, spaawncoords: tuple[int,int], damageMultiplier = 1):
        Bullet(owner.game_instance, owner, angle, self.range, spaawncoords)