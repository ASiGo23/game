import sys
import pygame
from pygame.locals import *

global screen

gameName = 'Untitled Game'

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption(gameName)

background = pygame.Surface((1000,500)).convert()
background.fill((250, 250, 250))
screen.blit(background, (0,0))

while True:
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                from Main import main
                main()
    clock.tick(60)