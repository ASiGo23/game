import math
import pygame
from pygame.locals import *
from Abstract import *
from Weapon import *
from Bullet import *
from botInput import *

global playerNum
playerNum = 0
class PhysicsCharacter(GravObj, Drawable, CollisionObj):
    def __init__(self):
        super().__init__()
        global playerNum
        self.playerNum = playerNum
        playerNum += 1
        self.health = 100
        self.isFiring = False
        self.isCrouching = False
        self.faceAngle = 0
        self.hitbox = pygame.Rect((50, 50, 10, 30))
        self.pWeapon = bulletLauncher(True, 5, 30, 5, 5, 500, (0, 0, 0))
        self.bot = bot(self)
    def updateCoord(self, deltaX, deltaY):
        self.hitbox.move_ip((deltaX, deltaY))

    def crouch(self,environmentObjects):
        self.hitbox.height = 15
        self.isCrouching = True
    
    def stand(self, environmentObjects):
        self.hitbox.height = 30
        self.hitbox.move_ip((0,-15))
        self.isCrouching = False

    def jump(self):
        self.yVelocity -= 15
    
    def moveOnX(self,environmentObjects,deltax):
        self.updateCoord(0,-1)
        self.updateCoord(deltax,0)
        for object in environmentObjects:
            if object.hitbox.colliderect(self.hitbox):
                self.updateCoord(0,1)
                if (abs(object.hitbox.top - self.hitbox.top) <= 10) and not self.isCrouching:
                    self.yVelocity = -7
                self.updateCoord(-deltax,0)
                self.updateCoord(0,-1)
        self.updateCoord(0,1)

    def fire(self,game_instance):
        self.pWeapon.fire(game_instance,self)
    def deal_damage(self,game_instance,damage):
        self.health -= damage
        if self.health <=0:
            game_instance.get_gameObjects().append(dead_character(self))
            game_instance.get_gameObjects().remove(self)
    def tick_action(self,game_instance):
        if self.pWeapon.fireDelay != 0:
            self.pWeapon.fireDelay -=1
    def mainMapUpdate(self,game_instance, canvas):
        pygame.draw.rect(canvas,(0,0,0),self.hitbox)
    def miniMapUpdate():
        pass

class dead_character():
    def __init__(self, character:PhysicsCharacter) -> None:
        self.respawnDelay = 0*60
        self.ghost = character
    
    def tick_action(self, game_instance):
        self.respawnDelay += -1
        if self.respawnDelay <=0:
            self.ghost.hitbox.topleft = (50,50)
            game_instance.get_gameObjects().append(self.ghost)
            game_instance.get_gameObjects().remove(self)


class platforms(Drawable, CollisionObj):
    def __init__(self, rect: Rect):
        self.hitbox = pygame.Rect(rect)
    def deal_damage(self,damage):
        pass
    def mainMapUpdate(self,game_instance, canvas):
        pygame.draw.rect(canvas,(0,0,0),self.hitbox)