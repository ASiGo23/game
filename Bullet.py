import pygame
from Abstract import *
from GameObj import PhysicsObj,GravObj

class Bullet(Drawable, PhysicsObj):
    def __init__(self, angle, spaawncoords: tuple[int,int]):
        from Main import gameObjects
        self.range = 500
        self.startcoord = spaawncoords
        self.endcoord = spaawncoords
        self.x = spaawncoords[0]
        self.y = spaawncoords[1]
        self.angle = angle
        gameObjects.append(self)
    def mainMapUpdate(self,canvas):
        pygame.draw.line(canvas, (0,0,0),self.startcoord, self.endcoord)
        from Main import gameObjects
        print(self.startcoord, gameObjects[0].body.center)
        gameObjects.remove(self)


class Grenade(Drawable, GravObj):
    pass