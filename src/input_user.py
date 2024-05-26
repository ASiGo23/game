import sys
import pygame
from pygame.locals import *
import pygame.key as key

from game_obj import *

def userInput(game_instance):
    from game_obj import platforms
    main = game_instance
    player = main.get_player()
    environmentObjects = main.get_type(platforms)

    for event in pygame.event.get():

        #Closes the window
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #Sees if the mouse's buttons are pressed to fire weapon
        if event.type == MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                player.isFiring = True

        #Stop firing if the mouse is not pressed
        elif event.type == MOUSEBUTTONUP:
            player.isFiring = False

        if event.type == KEYDOWN: 
            for platform in environmentObjects:

                #Sees if player can jump
                player_bottom = player.hitbox.centerx, player.hitbox.bottom
                hitbox_touch_bottom = platform.hitbox.collidepoint(player_bottom)
                if not hitbox_touch_bottom: continue

                #If the player is trying to jump, then call jump
                if event.key == K_UP: 
                    player.jump()
                    continue
                if event.key == K_w:
                    player.jump()
                    continue

            #Toggles the activation of the bot's "AI"
            if event.key == K_g:
                if main.botActive:
                    main.botActive = False
                else:
                    main.botActive = True

    if key.get_pressed()[pygame.K_LEFT]:
        player.moveOnX(-5)
    if key.get_pressed()[pygame.K_a]: 
        player.moveOnX(-5)
    if key.get_pressed()[pygame.K_RIGHT]: 
        player.moveOnX(5)
    if key.get_pressed()[pygame.K_d]:
        player.moveOnX(5)
    if key.get_pressed()[pygame.K_s]:
        player.crouch()
    elif player.isCrouching:
        player.stand()

    x,y = pygame.mouse.get_pos()
    player.aim = math.atan2(y-250,x-250)