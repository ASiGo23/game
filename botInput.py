import math
import pygame
from pygame.locals import *
import random

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
        playerlist = game_instance.get_type(PhysicsCharacter)
        for player in playerlist:
            if player.team == self.avatar.team:
                playerlist.remove(player)
        try:
            randomEnemy = playerlist[random.randint(0, len(playerlist)-1)]
            self.avatar.aim = math.atan2(
                randomEnemy.hitbox.centery - self.avatar.hitbox.centery,
                randomEnemy.hitbox.centerx - self.avatar.hitbox.centerx
            )
        except: pass
        if game_instance.botActive == True:
            self.avatar.isFiring = True
        else:
            self.avatar.isFiring = False
    def deactivate(self):
        self.active = False