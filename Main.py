#!/usr/bin/python

import pygame
from pygame import key,mouse,event
from pygame.locals import *
from GameObj import *
from ops import *
from ReadData import *
from UserInput import *
from botInput import *

def tickUpdate(game_instance):
    main = game_instance
    for character in main.get_gameObjects():
        if not isinstance(character, PhysicsCharacter):continue
        if character.pWeapon.fireDelay != 0:
            character.pWeapon.fireDelay -=1

def physics(game_instance):
    main = game_instance
    environmentObjects = main.get_environmentObjects()
    for player in main.get_players():
        #move the player according to the velocity incrementally
        for step in range(abs(player.yVelocity)):
            player.updateCoord(0,sign(player.yVelocity))
            for rect in environmentObjects:
                collidetop    = rect.hitbox.collidepoint(player.hitbox.midtop)
                collidebottom = rect.hitbox.collidepoint(player.hitbox.midbottom)
                if collidetop or collidebottom:
                    player.yVelocity = 0
                    player.updateCoord(0,-1 * sign(player.yVelocity))
                    break
        #check to see if player is on the ground
        #if not increase yVelocity and prevent from crouching
        onGround = False
        for platform in environmentObjects:
            collidebottom = platform.hitbox.collidepoint(player.hitbox.midbottom)
            if collidebottom:
                onGround = True
        if not onGround:
            player.yVelocity += 1

def characterActions(game_instance):
    main = game_instance
    for character in main.get_players():
        if character.isFiring == True:
            character.fire(game_instance)
            if character.pWeapon.isAuto == False:
                character.isFiring = False

def bulletPhysics(game_instance):
    for object in game_instance.get_gameObjects():
        if isinstance(object,Bullet):
            object.update_pos(game_instance)

def load(game_instance):
    main = game_instance
    player = main.get_player()
    background = main.get_background()
    canvas = main.get_canvas()
    screen = main.get_screen()
    gameObjects = main.get_gameObjects()
    
    background.fill((255,255,255))
    canvas.fill((255,255,255))
    screen.blit(background,(0,0))
    for active in gameObjects:
        active.mainMapUpdate(game_instance, canvas)
    xViewPort = gameObjects[player].hitbox.left - 250
    yViewPort = gameObjects[player].hitbox.top - 250
    screen.blit(canvas,(-xViewPort,-yViewPort))
    pygame.display.update()

class main():
    def __init__(self, screen:pygame.display, players, environmentObjects, player:int):
        self.players = players
        self.environmentObjects = environmentObjects
        self.gameObjects = players + environmentObjects
        self.xViewPort = 0
        self.yViewPort = 0
        self.player = player
        self.players[player].bot.deactivate()
        self.screen = screen
        self.canvas = pygame.Surface((1000,500)).convert()

        # Fill background
        self.background = pygame.Surface((1000,500)).convert()
        self.background.fill((250, 250, 250))

        # Blit everything to the screen
        self.screen.blit(self.background, (self.xViewPort, self.yViewPort))
        pygame.display.flip()

        clock = pygame.time.Clock()
        # Event loop
        while True:
            botInput(self)
            userInput(self)
            physics(self)
            characterActions(self)
            bulletPhysics(self)
            load(self)
            tickUpdate(self)
            clock.tick(60)
    def get_screen(self):
        return self.screen
    def get_canvas(self):
        return self.canvas
    def get_background(self):
        return self.background
    def get_player(self):
        return self.player
    def get_players(self):
        return self.players
    def get_environmentObjects(self):
        return self.environmentObjects
    def get_gameObjects(self):
        return self.gameObjects