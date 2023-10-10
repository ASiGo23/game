import sys
import pygame
from pygame.locals import *
from ReadData import *

gameName = 'Untitled Game'

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption(gameName)

background = pygame.Surface((1000,500)).convert()
background.fill((250, 250, 250))
screen.blit(background, (0,0))

Map = "Demo"

while True:
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        from Main import main
        game = main(screen)

        for object in ReadMap("Demo"):
            game.add_subject(object)
        for object in ReadSave():
            game.add_subject(object)

        game.player_set(0)

        game.run()
    clock.tick(20)

