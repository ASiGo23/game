from Abstract import *
from GameObj import PhysicsObj,GravObj

class Bullet(Drawable, PhysicsObj):
    def __init__(self, xVelocity: int, yVelocity:int):
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity


class Grenade(Drawable, GravObj):
    pass