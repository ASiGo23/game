import math
import pygame
from Abstract import *
from GameObj import PhysicsObj,GravObj

class Bullet(Drawable, PhysicsObj):
    def __init__(self, game_instance, owner, angle, range,spaawncoords: tuple[int,int]):
        self.owner = owner
        self.range = range
        self.startcoord = spaawncoords
        self.endcoord = spaawncoords
        self.x = spaawncoords[0]
        self.y = spaawncoords[1]
        self.angle = angle
        game_instance.get_gameObjects().append(self)
    def mainMapUpdate(self,game_instance, canvas):
        pygame.draw.line(canvas, (0,0,0),self.startcoord, self.endcoord)
        game_instance.get_gameObjects().remove(self)
    def update_pos(self,game_instance):
        from GameObj import platforms,PhysicsCharacter
        despawn = False
        xVelocity = math.cos(self.angle)
        yVelocity = math.sin(self.angle)
        for x in range(self.range):
            self.x += xVelocity
            self.y += yVelocity
            for rect in game_instance.get_type(platforms):
                if rect.hitbox.collidepoint(self.x, self.y):
                    despawn = True
                    self.endcoord = (self.x, self.y)
                    rect.deal_damage(50)
                    break
            for player in game_instance.get_type(PhysicsCharacter):
                if not player == self.owner:
                    if player.hitbox.collidepoint(self.x,self.y):
                        despawn = True
                        self.endcoord = (self.x, self.y)
                        player.deal_damage(game_instance, 50)
                        break
            if despawn == True: break
        self.endcoord = (self.x, self.y)


class Grenade(Drawable, GravObj):
    pass