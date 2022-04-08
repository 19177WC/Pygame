import pygame
import random
import pygame.freetype
from random import randint
from pygame import time
pygame.init()
#-----------------Variables--------------------#
window = pygame.display.set_mode((800, 480))
pygame.display.set_caption("Game Window")
y = 0
width = 100
height = 100
xRange = random.randint(50, 750)
yMovement = random.randint(5, 15)
RedColour = random.randint(0, 255)
GreenColour = random.randint(0, 255)
BlueColour = random.randint(0, 255)
colour = (RedColour, GreenColour , BlueColour)
bg = pygame.image.load('bg.jpg')
clock = pygame.time.Clock()
Circ = pygame.draw.circle(window, colour, (xRange, y), 25, 0)
Score = 0
scoreText = pygame.freetype.Font("yankclipper2.ttf", 50)
startText = pygame.freetype.Font("yankclipper2.ttf", 100)
pygame.display.flip()
#---------------------------- Methods ----------------------------
def redraw_GameWindow():
    global Circ
    window.blit(bg, (0,0)) # This will draw our background image at (0,0) .blit is short for block
    # transfer and allows us to add images to a surface, in this case the main window.
    Circ = pygame.draw.circle(window, colour, (xRange, y), 25, 0)
    scoreText.render_to(window, (10,10), "Score : {}" .format(Score), (0, 0, 0))
    pygame.display.update()
#---------------------------- Main Routine ----------------------------
run=True

while run:
    clock.tick(27)
    y += yMovement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif ( event.type == pygame.MOUSEBUTTONDOWN ):
            mouse_position = pygame.mouse.get_pos()             # Location of the mouse click
            if ( Circ.collidepoint( mouse_position ) ):   # Was that click inside our object
                Score = Score + 1
                y = 0
                xRange = random.randint(50, 750)
                yMovement = random.randint(10, 15)
                RedColour = random.randint(0, 255)
                GreenColour = random.randint(0, 255)
                BlueColour = random.randint(0, 255)
                colour = (RedColour, GreenColour, BlueColour)

    if y > 500:
        print("Your Score Is ", Score)
        print("GAME OVER MANNNN, GAME OVER!!!!")
        y = 0
        xRange = random.randint(50, 750)
        yMovement = random.randint(10, 15)
        RedColour = random.randint(0, 255)
        GreenColour = random.randint(0, 255)
        BlueColour = random.randint(0, 255)
        colour = (RedColour, GreenColour, BlueColour)
        break
    redraw_GameWindow()
