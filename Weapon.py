import math
import random
import pygame
from Bullet import *

class Weapon:
    def __init__(self,
    isAuto:bool, 
    fireRate:int,
    damage:int, 
    shots:int,
    acc:int,
    speed:int, 
    size:int, 
    range:int, 
    tracerColor: tuple[int,int,int]):
    
        #self.owner is set by the owner after creation
        self.owner = None
        self.isAuto = isAuto
        self.fireRate = fireRate
        self.fireDelay = 0
        self.damage = damage #unused
        self.shots = shots
        self.acc = acc
        self.speed = speed   #unused
        self.size = size     #unused
        self.tracer = tracerColor #unused
        self.range = range
    
    def fire(self):
        if self.fireDelay == 0:
            for shot in range(self.shots):
                dvariation = random.uniform((0-self.acc),(self.acc))
                rvariation = math.radians(dvariation)
                param_a = self.owner
                param_b = self.owner.aim + rvariation
                param_c = self.owner.hitbox.center
                self.spawnBullet(param_a, param_b, param_c)
            self.fireDelay = self.fireRate

    def spawnBullet(self, 
                    owner, 
                    angle, 
                    spaawncoords: tuple[int,int]):
        Bullet(owner.game_instance, owner, angle, self.range, spaawncoords)