class Drawable:
    pass

class CollisionObj:
    pass

class PhysicsObj:
    def __init__(self):
        self.xVelocity = 0
        self.yVelocity = 0

class GravObj(PhysicsObj):
    def __init__(self):
        super().__init__()