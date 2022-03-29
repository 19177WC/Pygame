import pygame
import random
from random import randint
from pygame import time
pygame.init()
window = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Game Window")
x = 500
y = 400
width = 100
height = 100
xRange = random.randint(0, 800)
yRange = random.randint(0, 500)
yMovement = 500

bg = pygame.image.load('bg.jpg')

clock = pygame.time.Clock()


colour = (255, 0 , 0)

pygame.display.flip()
#---------------------------- Methods ----------------------------
def redraw_GameWindow():
    window.blit(bg, (0,0)) # This will draw our background image at (0,0) .blit is short for block
    # transfer and allows us to add images to a surface, in this case the main window.
    pygame.draw.rect(window, colour, pygame.Rect(xRange, 500, 60, 60))
    pygame.display.update()
#---------------------------- Main Routine ----------------------------
run=True

while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    redraw_GameWindow()
