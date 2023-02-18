import math
import pygame
from pygame.locals import *
from Abstract import *
from Weapon import *
from Bullet import *

class PhysicsCharacter(GravObj, Drawable, CollisionObj):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.isFiring = False
        self.faceAngle = 0
        self.hitbox = pygame.Rect((50,50,10,30))
        self.pWeapon = bulletLauncher(True, 5,30,5,5,500,(0,0,0))
    def updateCoord(self,deltaX, deltaY):
        self.hitbox.move_ip((deltaX,deltaY))
    def moveOnX(self,deltax,bla):
        from Main import gameObjects
        self.updateCoord(0,-1)
        self.updateCoord(deltax,0)
        for object in gameObjects:
            if type(object) == platforms:
                if self.hitbox.colliderect(object.hitbox):
                    self.updateCoord(-deltax,0)
        self.updateCoord(0,1)

    def fire(self):
        self.pWeapon.fire(self)

    def mainMapUpdate(self,canvas):
        pygame.draw.rect(canvas,(0,0,0),self.hitbox)
    def miniMapUpdate():
        pass

class platforms(Drawable, CollisionObj):
    def __init__(self, rect: Rect):
        self.hitbox = pygame.Rect(rect)
    def mainMapUpdate(self,canvas):
        pygame.draw.rect(canvas,(0,0,0),self.hitbox)