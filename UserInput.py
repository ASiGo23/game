import sys
import pygame
from pygame.locals import *
import pygame.key as key

from GameObj import *

def userInput(game_instance):
    from GameObj import PhysicsCharacter,platforms
    main = game_instance
    player = main.get_player()
    environmentObjects = main.get_type(platforms)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                player.isFiring = True
        elif event.type == MOUSEBUTTONUP:
            player.isFiring = False
        if event.type == KEYDOWN: 
            for platform in environmentObjects:
                if not platform.hitbox.collidepoint(player.hitbox.centerx, player.hitbox.bottom): continue
                if event.key == K_UP: 
                    player.jump()
                    continue
                if event.key == K_w:
                    player.jump()
                    continue
            if event.key == K_g:
                if main.botActive:
                    main.botActive = False
                else:
                    main.botActive = True

    if key.get_pressed()[pygame.K_LEFT]:
        player.moveOnX(environmentObjects,-5)
    if key.get_pressed()[pygame.K_a]: 
        player.moveOnX(environmentObjects,-5)
    if key.get_pressed()[pygame.K_RIGHT]: 
        player.moveOnX(environmentObjects, 5)
    if key.get_pressed()[pygame.K_d]:
        player.moveOnX(environmentObjects, 5)
    if key.get_pressed()[pygame.K_s]:
        player.crouch(environmentObjects)
    elif player.isCrouching:
        player.stand(environmentObjects)

    x,y = pygame.mouse.get_pos()
    player.aim = math.atan2(y-250,x-250)