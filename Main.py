#!/usr/bin/python

import sys
import pygame
from pygame import key,mouse,event
from pygame.locals import *
from GameObj import *
from ops import *
from MapRead import *

def setup():
    global screen
    global background
    global canvas
    global gameObjects
    global player
    global xViewPort
    global yViewPort

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

    gameObjects = ReadMap("Demo")
    player = 0

def userInput():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if not event.type == KEYDOWN: continue
        for platform in gameObjects:
            if not type(platform) == platforms: continue
            if not gameObjects[player].body.colliderect(platform.shape): continue
            if event.key == K_UP: gameObjects[player].yVelocity -= 15
            if event.key == K_w:  gameObjects[player].yVelocity -= 15

    if key.get_pressed()[pygame.K_LEFT]:
        gameObjects[player].moveOnX(-5,0)
    if key.get_pressed()[pygame.K_a]: 
        gameObjects[player].moveOnX(-5,0)
    if key.get_pressed()[pygame.K_RIGHT]: 
        gameObjects[player].moveOnX(5,0)
    if key.get_pressed()[pygame.K_d]:
        gameObjects[player].moveOnX(5,0)
    if mouse.get_pressed()[0]:
        gameObjects[player].spawnbullet()

def physics():
    for object in gameObjects:
        if not isinstance(object, GravObj): continue

        object.updateCoord(0,1)
        for rect in gameObjects:
            if not type(rect) == platforms: continue
            if object.body.colliderect(rect.shape):
                object.updateCoord(0,-1)
        onGround = False
        for rect in gameObjects:
            if not type(rect) == platforms: continue
            if not object.body.colliderect(rect.shape): continue
            onGround = True
        if (not onGround) and isinstance(object,GravObj):
            object.yVelocity = object.yVelocity + 1
        for step in range(abs(object.yVelocity)):
            object.updateCoord(0,sign(object.yVelocity))
            for rect in gameObjects:
                if not isinstance(rect, platforms): continue

                if not object.body.colliderect(rect.shape): continue
                object.yVelocity = 0
                object.updateCoord(0,-1 * sign(object.yVelocity))
                break

def load():
    global xViewPort
    background.fill((255,255,255))
    canvas.fill((255,255,255))
    screen.blit(background,(0,0))
    for active in gameObjects:
        active.mainMapUpdate(canvas)
    xViewPort = gameObjects[player].body.left - 250
    yViewPort = gameObjects[player].body.top - 250
    screen.blit(canvas,(-xViewPort,-yViewPort))
    pygame.display.update()

def main():
    setup()
    clock = pygame.time.Clock()
    # Event loop
    while True:
        userInput()
        physics()
        load()
        clock.tick(60)


if __name__ == '__main__': main()