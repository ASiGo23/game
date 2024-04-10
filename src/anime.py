import io
import sys
import pygame
import cairosvg
from pygame.locals import *

pygame.init()

screen  = pygame.display.set_mode((500,1000))
background = pygame.Surface((500,1000)).convert()
background.fill((255, 255, 255))
canvas = pygame.Surface((250,320)).convert()

image = cairosvg.svg2png(url='custom.svg', output_width=500)
image = io.BytesIO(image)
image = pygame.image.load(image)

# Blit everything to the screen
screen.blit(background, (0,0))
screen.blit(image,(0,0))
pygame.display.flip()
while True:
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(1)