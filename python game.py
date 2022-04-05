import pygame
import random
from random import randint
from pygame import time
pygame.init()
window = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Game Window")
x = 500
y = 0
width = 100
height = 100
xRange = random.randint(0, 800)
yMovement = random.randint(5, 15)
RedColour = random.randint(0, 255)
GreenColour = random.randint(0, 255)
BlueColour = random.randint(0, 255)
colour = (RedColour, GreenColour , BlueColour)
bg = pygame.image.load('bg.jpg')
clock = pygame.time.Clock()
Rect = pygame.draw.rect(window, colour, (xRange, y, 50, 50))



pygame.display.flip()
#---------------------------- Methods ----------------------------
def redraw_GameWindow():
    global Rect
    window.blit(bg, (0,0)) # This will draw our background image at (0,0) .blit is short for block
    # transfer and allows us to add images to a surface, in this case the main window.
    Rect = pygame.draw.rect(window, colour, (xRange, y, 50, 50))
    pygame.display.update()
#---------------------------- Main Routine ----------------------------
run=True

while run:
    clock.tick(27)
    y += yMovement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif ( event.type == pygame.MOUSEBUTTONUP ):
            mouse_position = pygame.mouse.get_pos()             # Location of the mouse-click
            if ( Rect.collidepoint( mouse_position ) ):   # Was that click inside our rectangle
                print( "hit" )

    if y > 500:
        y = 0
        xRange = random.randint(0, 800)
        yMovement = random.randint(5, 15)
        RedColour = random.randint(0, 255)
        GreenColour = random.randint(0, 255)
        BlueColour = random.randint(0, 255)
        colour = (RedColour, GreenColour, BlueColour)
    redraw_GameWindow()