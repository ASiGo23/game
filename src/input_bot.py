import math
import pygame
from pygame.locals import *
import random

def botInput(game_instance):
    from game_obj import player_character
    for bot in game_instance.get_type(player_character):
        if bot.bot.active == True:
            bot.bot.calculate_moves()

class bot:
    def __init__(self,avatar):
        self.game_instance = None
        self.avatar = avatar
        self.active = True
    def calculate_moves(self):
        from game_obj import player_character,platforms
        self.avatar.moveOnX(2)
        playerlist = self.game_instance.get_type(player_character)
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
        if self.game_instance.botActive == True:
            self.avatar.isFiring = True
        else:
            self.avatar.isFiring = False
    def deactivate(self):
        self.active = False