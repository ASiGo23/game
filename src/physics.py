from pygame import Rect, Vector2
from math import sin, cos, atan2, pow, sqrt

global grav_constant; grav_constant = 1
global grav_accel; grav_accel = 1

class physics_subject:
    subjects = []

    def __init__(self, 
                 mass:int = 5,
                 velocity: Vector2 = Vector2(),
                 anchored: bool = False,
                 gravity: bool = True):
        self.mass = mass
        self.velocity = velocity
        self.anchored = anchored
        self.gravity = gravity

    def tick_action(self):
        if self.anchored:
            return
        if self.gravity:
            self.velocity.y += grav_accel
class character(physics_subject):
    def __init__(self, rect: Rect):
        super().__init__(5, 0, 0, False, True)
        super().subjects.append(self)
        self.rect = rect
    def tick_action(self):
        super().tick_action()