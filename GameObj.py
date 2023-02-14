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
        self.faceAngle = 0
        self.body = pygame.Rect((50,50,10,30))
        self.pWeapon = bulletLauncher(5,5,5,(0,0,0))
    def updateCoord(self,deltaX, deltaY):
        self.body.move_ip((deltaX,deltaY))
    def moveOnX(self,deltax,bla):
        from Main import gameObjects
        self.updateCoord(0,-1)
        self.updateCoord(deltax,0)
        for object in gameObjects:
            if type(object) == platforms:
                if self.body.colliderect(object.shape):
                    self.updateCoord(-deltax,0)
        self.updateCoord(0,1)
    def spawnbullet(self):
        x,y = pygame.mouse.get_pos()
        self.pWeapon.spawnBullet(math.atan((y-250)/(x-250)),self.body.center)
    def mainMapUpdate(self,canvas):
        pygame.draw.rect(canvas,(0,0,0),self.body)
    def miniMapUpdate():
        pass

class platforms(Drawable, CollisionObj):
    def __init__(self, rect: Rect):
        self.shape = pygame.Rect(rect)
    def mainMapUpdate(self,canvas):
        pygame.draw.rect(canvas,(0,0,0),self.shape)