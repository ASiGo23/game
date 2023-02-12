import pygame
from Bullet import *

class missleLauncher:
    def __init__(self, damage:int, speed:int, size:int, tracerColor: tuple[int,int,int]):
        self.missleDamage = damage
        self.missleSpeed = speed
        self.missleSize = size
        self.tracer = tracerColor
    def spawnBullet(self, angle, spaawncoords: tuple[int,int], damageMultiplier = 1):
        Bullet(0,0,spaawncoords)