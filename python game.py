import pygame                                                   # "Pygame is a cross-platform set of Python modules designed for writing video games." - Wikipedia
import random
import pygame.freetype
from pygame import time
pygame.init()
#-----------------Variables--------------------#
window = pygame.display.set_mode((800, 480))                    # Window Size
pygame.display.set_caption("Falling Balls")                     # Name of the game
y = 0                                                           # Ball Starting Position
xRange = random.randint(50, 750)                                # Random start on X axis
yMovement = random.randint(5, 15)                               # Random Downwards movement
#----------Randomises Colour----------#
RedColour = random.randint(0, 255)
GreenColour = random.randint(0, 255)
BlueColour = random.randint(0, 255)
colour = (RedColour, GreenColour , BlueColour)                  # Combines the three random values for R,G,B to make every possible colour

bg = pygame.image.load('bg.jpg')                                # Background
clock = pygame.time.Clock()
Score = 0
End  = False
Start = True
Circ = pygame.draw.circle(window, colour, (xRange, y), 25, 0)   # Code for the circle
scoreText = pygame.freetype.Font("yankclipper2.ttf", 50)        # Text that displays the score
startText = pygame.freetype.Font("yankclipper2.ttf", 100)       # Start Text
endText = pygame.freetype.Font("yankclipper2.ttf", 100)         # End Text
pygame.display.flip()
#---------------------------- Methods ----------------------------#
def redraw_GameWindow():
    global Circ                                                 # You need globals so your variables will work inside the dictionary(def)
    global y
    global yMovement
    window.blit(bg, (0, 0))                                      # Draws Background
    Circ = pygame.draw.circle(window, colour, (xRange, y), 25, 0)

    if End == False and Start == False:                          # If statements are when if (event) happens, the code inside it will play
                                                                 # When the game isnt at the end screen or start screen it makes it so score text doesnt display
        scoreText.render_to(window, (10,10), "Score : {}" .format(Score), (0, 0, 0))
    if End == True:                                              # When the game is at the end Screen it Shows Score and Asks whether to play again after losing the game
        endText.render_to(window, (100, 150), "Your Score is {}".format(Score), (0, 0, 0))
        endText.render_to(window, (10, 250), "Press Space To Play Again".format(Score), (0, 0, 0))
        y = -25                                                  # makes it so the ball isnt visible while end screen is going
        yMovement = 0                                            # sets movement to zero
    if Start == True:                                            # if the start screen is showing then the following code will happen
        startText.render_to(window, (150, 150), "Press Space To Play", (0, 0, 0))
        y = -25
        yMovement = 0
    pygame.display.update()
#---------------------------- Main Routine ----------------------------
run = True

while run:
    clock.tick(27)
    keys = pygame.key.get_pressed()                              # Code to detect when a key on the keyboard is pressed
    y += yMovement                                               # Will make the circle move down the screen because the Y value will be increasing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif ( event.type == pygame.MOUSEBUTTONDOWN ):
            mouse_position = pygame.mouse.get_pos()             # Location of the mouse click
            if ( Circ.collidepoint( mouse_position ) ):         # Was that click inside our circle
                Score = Score + 1                               # Adds +1 to the score whenever the Circle is clicked
                y = 0
                xRange = random.randint(50, 750)
                yMovement = random.randint(10, 15)
                RedColour = random.randint(0, 255)
                GreenColour = random.randint(0, 255)
                BlueColour = random.randint(0, 255)
                colour = (RedColour, GreenColour, BlueColour)
        if keys[pygame.K_SPACE]:                                # if space bar is pressed during start or end screen it will start playing a new game
            if End == True or Start == True:                    # When end = false and when start = false is when the actual game is being played
                End = False
                Start = False
                yMovement = random.randint(5, 15)
                Score = 0                                       # Resets score to prepare for next game
    if y > 500:                                                 # Goes to End Screen and prepares for next game
        y = 0
        xRange = random.randint(50, 750)
        yMovement = random.randint(10, 15)
        RedColour = random.randint(0, 255)
        GreenColour = random.randint(0, 255)
        BlueColour = random.randint(0, 255)
        colour = (RedColour, GreenColour, BlueColour)
        End = True
    redraw_GameWindow()                                         # This means that the entire "while run" code is linked to the redraw_GameWindow