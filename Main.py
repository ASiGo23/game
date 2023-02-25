#!/usr/bin/python

import pygame
from pygame import key,mouse,event
from pygame.locals import *
from GameObj import *
from ops import *
from ReadData import *
from UserInput import *

def tickUpdate():
    for character in gameObjects:
        if not isinstance(character, PhysicsCharacter):continue
        if character.pWeapon.fireDelay != 0:
            character.pWeapon.fireDelay -=1

def physics(players,environmentObjects):
    for player in players:
        player.updateCoord(0,-1)
        for rect in environmentObjects:
            if player.hitbox.colliderect(rect.hitbox):
                player.updateCoord(0,1)
                player.yVelocity = 0
        player.updateCoord(0,1)
        onGround = False
        for platform in environmentObjects:
            if platform.hitbox.collidepoint(player.hitbox.midbottom):
                onGround = True
            if platform.hitbox.collidepoint(player.hitbox.midtop):
                onGround = True
        if (not onGround) and isinstance(player,GravObj):
            player.yVelocity = player.yVelocity + 1
        for step in range(abs(player.yVelocity)):
            player.updateCoord(0,sign(player.yVelocity))
            for rect in gameObjects:
                if not isinstance(rect, platforms): continue
                if not player.hitbox.colliderect(rect.hitbox): continue
                player.yVelocity = 0
                player.updateCoord(0,-1 * sign(player.yVelocity))
                break

def characterActions():
    for character in gameObjects:
        if not isinstance(character, PhysicsCharacter): continue
        if character.isFiring == True:
            character.fire()
            if character.pWeapon.isAuto == False:
                character.isFiring = False

def bulletPhysics():
    for object in gameObjects:
        despawn = False
        if not isinstance(object,Bullet): continue
        xVelocity = math.cos(object.angle)
        yVelocity = math.sin(object.angle)
        for x in range(object.range):
            object.x += xVelocity
            object.y += yVelocity
            for rect in gameObjects:
                if not isinstance(rect,platforms):continue
                if not rect.hitbox.collidepoint(object.x, object.y):continue
                despawn = True
                object.endcoord = (object.x, object.y)
                break
            if despawn == True: break
        object.endcoord = (object.x, object.y)

def load():
    global xViewPort
    background.fill((255,255,255))
    canvas.fill((255,255,255))
    screen.blit(background,(0,0))
    for active in gameObjects:
        active.mainMapUpdate(canvas)
    xViewPort = gameObjects[player].hitbox.left - 250
    yViewPort = gameObjects[player].hitbox.top - 250
    screen.blit(canvas,(-xViewPort,-yViewPort))
    pygame.display.update()

def main(environmentObjects:list, players:list, events:list = []):
    global screen
    global background
    global canvas
    global gameObjects
    global player
    global xViewPort
    global yViewPort

    gameObjects = players + environmentObjects
    xViewPort = 0
    yViewPort = 0
    from Launcher import screen

    # Fill background
    background = pygame.Surface((1000,500)).convert()
    background.fill((250, 250, 250))

    canvas = pygame.Surface((1000,500)).convert()

    # Blit everything to the screen
    screen.blit(background, (xViewPort, yViewPort))
    pygame.display.flip()

    player = 0

    clock = pygame.time.Clock()
    # Event loop
    while True:
        userInput(gameObjects,players,environmentObjects,player)
        physics(players,environmentObjects)
        characterActions()
        bulletPhysics()
        load()
        tickUpdate()
        print(players[player].yVelocity)
        clock.tick(60)


if __name__ == '__main__': main()