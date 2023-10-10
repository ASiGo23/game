#!/usr/bin/python

from functools import singledispatchmethod
import pygame
from pygame import key,mouse,event
from pygame.locals import *
from GameObj import *
from ops import *
from ReadData import *
from UserInput import *
from botInput import *

def tickUpdate(game_instance):
    for object in game_instance.get_game_objects():
        try: object.tick_action()
        except: pass

def physics(game_instance):
    main = game_instance
    environmentObjects = main.get_type(platforms)
    for player in main.get_type(PhysicsCharacter):
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
    for character in main.get_type(PhysicsCharacter):
        if character.isFiring == True:
            character.fire()
            if character.pWeapon.isAuto == False:
                character.isFiring = False

def bulletPhysics(game_instance):
    for object in game_instance.get_type(Bullet):
        object.update_pos()

def load(game_instance):
    main = game_instance
    player = main.get_player()
    background = main.get_background()
    canvas = main.get_canvas()
    screen = main.get_screen()
    game_objects = main.get_game_objects()
    drawable_objects = main.get_type(Drawable)
    
    background.fill((255,255,255))
    canvas.fill((255,255,255))
    screen.blit(background,(0,0))
    for active in drawable_objects:
        active.mainMapUpdate(canvas)
    xViewPort = player.hitbox.left - 250
    yViewPort = player.hitbox.top - 250
    screen.blit(canvas,(-xViewPort,-yViewPort))
    pygame.display.update()

class main():
    def __init__(self, screen:pygame.Surface):

        self.player = None
        self.botActive = False
        self.xViewPort = 0
        self.yViewPort = 0
        self.screen = screen
        self.canvas = pygame.Surface((1000,500)).convert()

        self.character_list = []
        self.game_objects= []

        # Fill background
        self.background = pygame.Surface((1000,500)).convert()
        self.background.fill((250, 250, 250))

        # Blit everything to the screen
        self.screen.blit(self.background, (self.xViewPort, self.yViewPort))
        pygame.display.flip()

    @singledispatchmethod
    def add_subject(self, subject:PhysicsCharacter):
        self.character_list.append(subject)
        self.game_objects.append(subject)
        subject.game_instance = self
        subject.bot.game_instance = self
        

    @add_subject.register
    def _(self, subject:platforms):
        self.game_objects.append(subject)

    def player_set(self, num:int):
        self.player = self.character_list[num]
        self.player.bot.deactivate()

    def run(self):
        clock = pygame.time.Clock()
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
    def update_player(self, new_player:PhysicsCharacter):
        self.player.bot.active = True
        self.player = new_player
        self.player.bot.active = False

    def get_type(self,input_class:type):
        buffer = []
        for object in self.game_objects:
            if isinstance(object,input_class):
                buffer.append(object)
        return buffer
    def get_game_objects(self):
        return self.game_objects