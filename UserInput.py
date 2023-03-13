import sys
import pygame
from pygame.locals import *
import pygame.key as key

from GameObj import *

def userInput(game_instance):
    from GameObj import PhysicsCharacter,platforms
    main = game_instance
    player = main.get_player()
    players = main.get_type(PhysicsCharacter)
    environmentObjects = main.get_type(platforms)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                players[player].isFiring = True
        elif event.type == MOUSEBUTTONUP:
            players[player].isFiring = False
        if not event.type == KEYDOWN: continue
        for platform in environmentObjects:
            if not platform.hitbox.collidepoint(players[player].hitbox.centerx,players[player].hitbox.bottom): continue
            if event.key == K_UP: 
                players[player].jump()
            if event.key == K_w:
                players[player].jump()

    if key.get_pressed()[pygame.K_LEFT]:
        players[player].moveOnX(environmentObjects,-5)
    if key.get_pressed()[pygame.K_a]: 
        players[player].moveOnX(environmentObjects,-5)
    if key.get_pressed()[pygame.K_RIGHT]: 
        players[player].moveOnX(environmentObjects, 5)
    if key.get_pressed()[pygame.K_d]:
        players[player].moveOnX(environmentObjects, 5)
    if key.get_pressed()[pygame.K_s]:
        players[player].crouch(environmentObjects)
    elif players[player].isCrouching:
        players[player].stand(environmentObjects)