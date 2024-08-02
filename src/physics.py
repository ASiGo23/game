from pygame import Rect, Vector2
from math import sin, cos, atan2, pow, sqrt
from adv_poly import adv_polygon, adv_rect
import double_cheese_burger as dcb

global grav_constant; grav_constant = 1
global grav_accel; grav_accel = 1
global tick; tick = 1/60

class physics_subject:
    subjects = dcb.double_linked_list()

    def __init__(self, 
                 shape:adv_polygon,
                 mass:int = 5,
                 anchored: bool = False,
                 gravity: bool = True):
        self.shape = shape
        self.mass = mass
        self.anchored = anchored
        self.gravity = gravity

    def tick_action():
        for subject in super().subjects:
            if subject.gravity is True:
                subject.shape.velocity[1] += grav_accel 
        
        collisions = {}
        for subject_1 in super().subjects:
            for subject_2 in super().subjects:
                if subject_1 != subject_2:
                    time = subject_1.shape.collide_poly(subject_2.shape)
                    collisions.update(time, subject_1, subject_2) 
        
          

class character(physics_subject):
    def __init__(self, rect: adv_rect):
        super().__init__(
            shape = rect, 
            mass = 5, 
            anchored = False, 
            gravity = True)
        super().subjects.append(self) 
    def tick_action(self):
        super().tick_action()