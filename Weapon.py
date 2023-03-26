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
    
        self.owner = None
        self.isAuto = isAuto
        self.fireRate = fireRate
        self.fireDelay = 0
        self.missleDamage = damage
        self.missleSpeed = speed
        self.missleSize = size
        self.tracer = tracerColor
        self.range = range
    
    def fire(self, game_instance):
        if self.fireDelay == 0:
            self.spawnBullet(game_instance, self.owner, self.owner.aim, self.owner.hitbox.center)
            self.fireDelay = self.fireRate

    def spawnBullet(self, game_instance, owner, angle, spaawncoords: tuple[int,int], damageMultiplier = 1):
        Bullet(game_instance, owner, angle, self.range, spaawncoords)