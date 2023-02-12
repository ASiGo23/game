import pygame
from Abstract import *
from GameObj import PhysicsObj,GravObj

class Bullet(Drawable, PhysicsObj):
    def __init__(self, xVelocity: int, yVelocity:int, spaawncoords: tuple[int,int]):
        from Main import gameObjects
        self.startcoord = spaawncoords
        self.endcoord = 0,0
        self.x = spaawncoords[0]
        self.y = spaawncoords[1]
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        gameObjects.append(self)
    def mainMapUpdate(self,canvas):
        pygame.draw.line(canvas, (0,0,0),self.startcoord, self.endcoord)
        from Main import gameObjects
        gameObjects.remove(self)


class Grenade(Drawable, GravObj):
    pass