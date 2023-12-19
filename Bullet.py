import math
import pygame
from Abstract import *
from GameObj import PhysicsObj,GravObj

class Bullet(Drawable, PhysicsObj):
    def __init__(self, game_instance, owner, angle, range,spaawncoords: tuple[int,int]):
        self.game_instance = game_instance
        self.owner = owner
        self.range = range
        self.startcoord = spaawncoords
        self.endcoord = spaawncoords
        self.x = spaawncoords[0]
        self.y = spaawncoords[1]
        self.angle = angle
        game_instance.get_game_objects().append(self)
 
    def mainMapUpdate(self, canvas):
        pygame.draw.line(canvas, (0,0,0),self.startcoord, self.endcoord)
        self.game_instance.get_game_objects().remove(self)

    def update_pos(self):
        from GameObj import platforms,player_character
        despawn = False
        xVelocity = math.cos(self.angle)
        yVelocity = math.sin(self.angle)
        for x in range(self.range):
            self.x += xVelocity
            self.y += yVelocity
            for rect in self.game_instance.get_type(platforms):
                if rect.hitbox.collidepoint(self.x, self.y):
                    despawn = True
                    self.endcoord = (self.x, self.y)
                    rect.deal_damage(50)
                    break
            for player in self.game_instance.get_type(player_character):
                is_self = player == self.owner
                is_team = player.team == self.owner.team
                if ((not is_self) and (not is_team)):
                    if player.hitbox.collidepoint(self.x,self.y):
                        despawn = True
                        self.endcoord = (self.x, self.y)
                        player.deal_damage(50)
                        print("player:",player.team)
                        print("owner",self.owner.team)
                        break
            if despawn == True: break
        self.endcoord = (self.x, self.y)


class Grenade(Drawable, GravObj):
    pass