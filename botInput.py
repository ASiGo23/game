import math
import pygame
from pygame.locals import *

def botInput(game_instance):
    from GameObj import PhysicsCharacter
    for bot in game_instance.get_type(PhysicsCharacter):
        if bot.bot.active == True:
            bot.bot.calculate_moves(game_instance)

class bot:
    def __init__(self,avatar):
        self.avatar = avatar
        self.active = True
    def calculate_moves(self,game_instance):
        from GameObj import PhysicsCharacter,platforms
        self.avatar.moveOnX(game_instance.get_type(platforms),2)
        print(self.avatar.playerNum)
        if not pygame.key.get_pressed()[pygame.K_o]: return
        player = game_instance.get_player()
        self.avatar.aim = math.atan2(
            self.avatar.hitbox.centery-player.hitbox.centery,
            self.avatar.hitbox.centery-player.hitbox.centerx
        )
        self.avatar.isFiring = True
    def deactivate(self):
        self.active = False