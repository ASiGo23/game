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
    def __init__(self, pWeapon, maxHealth = 100, team = 0) -> None:
        super().__init__()
        self.game_instance = None

        global playerNum
        self.playerNum = playerNum
        playerNum += 1

        self.health = maxHealth
        self.team = team
        self.isFiring = False
        self.isCrouching = False
        self.aim = 0
        self.faceAngle = 0
        self.hitbox = pygame.Rect((50, 50, 10, 30))
        self.pWeapon = pWeapon
        self.pWeapon.owner = self
        self.bot = bot(self)

    def updateCoord(self, deltaX, deltaY) -> None:
        self.hitbox.move_ip((deltaX, deltaY))

    def crouch(self) -> None:
        self.hitbox.height = 15
        self.isCrouching = True
    
    def stand(self) -> None:
        self.hitbox.height = 30
        self.hitbox.move_ip((0,-15))
        self.isCrouching = False

    def jump(self) -> None:
        self.yVelocity -= 15
    
    def moveOnX(self,deltax) -> None:
        environmentObjects = self.game_instance.get_type(platforms)
        self.updateCoord(0,-1)
        self.updateCoord(deltax,0)
        for object in environmentObjects:
            if object.hitbox.colliderect(self.hitbox):
                self.updateCoord(0,1)
                distance = abs(object.hitbox.top - self.hitbox.top)
                if (distance <= 10) and not self.isCrouching:
                    self.yVelocity = -7
                self.updateCoord(-deltax,0)
                self.updateCoord(0,-1)
        self.updateCoord(0,1)

    def fire(self) -> None:
        self.pWeapon.fire()

    def deal_damage(self,damage) -> None:
        self.health -= damage
        if self.health <=0:
            game_objects = self.game_instance.get_game_objects()
            game_objects.append(dead_character(self, self.game_instance))
            game_objects.remove(self)

    def tick_action(self) -> None:
        if self.pWeapon.fireDelay != 0:
            self.pWeapon.fireDelay -=1

    def mainMapUpdate(self, canvas) -> None:
        pygame.draw.rect(canvas,(0,0,0),self.hitbox)

    def miniMapUpdate() -> None:
        pass

class dead_character():
    def __init__(self, character:PhysicsCharacter, game_instance) -> None:
        self.game_instance = game_instance
        self.respawnDelay = 1*60
        self.ghost = character
    
    def tick_action(self) -> None:
        self.respawnDelay += -1
        if self.respawnDelay <=0:
            self.ghost.hitbox.topleft = (50,50)
            self.game_instance.get_game_objects().append(self.ghost)
            self.game_instance.get_game_objects().remove(self)


class platforms(Drawable, CollisionObj):
    def __init__(self, rect: Rect):
        self.hitbox = pygame.Rect(rect)
    def deal_damage(self,damage):
        pass
    def mainMapUpdate(self, canvas):
        pygame.draw.rect(canvas,(0,0,0),self.hitbox)