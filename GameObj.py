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
        #Bug: When player is within 5 units of the edge of an object when falling and moving on x, 
        # the player will fall through the platform
        for object in environmentObjects:
            if object.hitbox.colliderect(self.hitbox):
                if self.hitbox.collidepoint(object.hitbox.midleft):
                    self.yVelocity -= 4
                if self.hitbox.collidepoint(object.hitbox.midright):
                    self.yVelocity -= 4
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