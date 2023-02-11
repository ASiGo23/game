import pygame
from pygame.locals import *
from Abstract import *

class PhysicsObj:
    def __init__(self):
        self.xVelocity = 0
        self.yVelocity = 0

class GravObj(PhysicsObj):
    def __init__(self):
        super().__init__()

from Weapon import *
from Bullet import *

class PhysicsCharacter(GravObj, Drawable, CollisionObj):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.faceAngle = 0
        self.body = pygame.Rect((50,50,10,30))
        self.pWeapon = missleLauncher(5,5,5,(0,0,0))
    def updateCoord(self,deltaX, deltaY):
        self.body.move_ip((deltaX,deltaY))
    def moveOnX(self,deltax,bla):
        from Main import gameObjects
        self.updateCoord(0,-1)
        self.updateCoord(deltax,0)
        for object in gameObjects:
            if type(object) == platforms:
                print("here")
                if self.body.colliderect(object.shape):
                    self.updateCoord(-deltax,0)
        self.updateCoord(0,1)
    def spawnbullet(self):
        x,y = pygame.mouse.get_pos()
        print(x,y)
        #self.pWeapon.spawnBullet()
    def mainMapUpdate(self,canvas):
        pygame.draw.rect(canvas,(0,0,0),self.body)
    def miniMapUpdate():
        pass

class platforms(Drawable, CollisionObj):
    def __init__(self, rect: Rect):
        self.shape = rect
    def mainMapUpdate(self,canvas):
        pygame.draw.rect(canvas,(0,0,0),self.shape)