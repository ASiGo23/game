import sys
import pygame
from pygame.locals import *
import pygame.key as key

from GameObj import *

def userInput(gameObjects: list, player:int):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            gameObjects[player].isFiring = True
        elif event.type == MOUSEBUTTONUP:
            gameObjects[player].isFiring = False
        if not event.type == KEYDOWN: continue
        for platform in gameObjects:
            if not type(platform) == platforms: continue
            if not gameObjects[player].hitbox.colliderect(platform.hitbox): continue
            if event.key == K_UP: 
                gameObjects[player].jump()
            if event.key == K_w:
                gameObjects[player].jump()


    if key.get_pressed()[pygame.K_LEFT]:
        gameObjects[player].moveOnX(-5)
    if key.get_pressed()[pygame.K_a]: 
        gameObjects[player].moveOnX(-5)
    if key.get_pressed()[pygame.K_RIGHT]: 
        gameObjects[player].moveOnX(5)
    if key.get_pressed()[pygame.K_d]:
        gameObjects[player].moveOnX(5)
    if key.get_pressed()[pygame.K_s]:
        gameObjects[player].crouch()
    elif gameObjects[player].isCrouching:
        gameObjects[player].stand()