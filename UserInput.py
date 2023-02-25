import sys
import pygame
from pygame.locals import *
import pygame.key as key

from GameObj import *

def userInput(gameObjects: list, players:list, environmentObjects:list, player:int):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                gameObjects[player].isFiring = True
        elif event.type == MOUSEBUTTONUP:
            gameObjects[player].isFiring = False
        if not event.type == KEYDOWN: continue
        for platform in environmentObjects:
            if not platform.hitbox.collidepoint(players[player].hitbox.centerx,players[player].hitbox.bottom): continue
            if event.key == K_UP: 
                gameObjects[player].jump()
            if event.key == K_w:
                gameObjects[player].jump()

    if key.get_pressed()[pygame.K_LEFT]:
        gameObjects[player].moveOnX(environmentObjects,-5)
    if key.get_pressed()[pygame.K_a]: 
        gameObjects[player].moveOnX(environmentObjects,-5)
    if key.get_pressed()[pygame.K_RIGHT]: 
        gameObjects[player].moveOnX(environmentObjects, 5)
    if key.get_pressed()[pygame.K_d]:
        gameObjects[player].moveOnX(environmentObjects, 5)
    if key.get_pressed()[pygame.K_s]:
        gameObjects[player].crouch()
    elif gameObjects[player].isCrouching:
        gameObjects[player].stand()