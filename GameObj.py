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
        self.isCrouching = False
        self.faceAngle = 0
        self.hitbox = pygame.Rect((50,50,10,30))
        self.pWeapon = bulletLauncher(True, 5,30,5,5,500,(0,0,0))
    def updateCoord(self,deltaX, deltaY):
        self.hitbox.move_ip((deltaX,deltaY))

    def crouch(self):
        self.hitbox.height = 15
        self.isCrouching = True
    
    def stand(self):
        self.hitbox.height = 30
        self.hitbox.move_ip((0,-15))
        self.isCrouching = False

    def jump(self):
        self.yVelocity -= 15
    
    def moveOnX(self,environmentObjects,deltax):
        self.updateCoord(0,-1)
        self.updateCoord(deltax,0)
        for object in environmentObjects:
            if object.hitbox.colliderect(self.hitbox):
                self.updateCoord(0,1)
                if abs(object.hitbox.top - self.hitbox.top) <= 10:
                    self.yVelocity -= 7
                self.updateCoord(-deltax,0)
                self.updateCoord(0,-1)
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