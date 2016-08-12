"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
PURPLE = (160, 32, 240)



pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("ROOM MOVER")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# WRITE YOUR CODE HERE
colors = [BLACK, GREEN, BLUE, RED]

def random_color():
    return random.choice(colors)
# def holding():
#     global held, coordinates
#     if held:
#         coordinates = pygame.mouse.get_pos()


length_of_room = int(input("Enter length of room"))
width_of_room = int(input("Enter width of room"))



gitrect = []

# -------- Main Program Loop -----------

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mouse.get_pressed()
            length_of_furniture = int(input("enter length of furniture"))
            width_of_furniture = int(input("enter width of furniture"))
            gitrect.append([random_color(), width_of_furniture, length_of_furniture])
        # print (gitrect)

        # if event.type == MOUSEBUTTONDOWN:
        #     coordinates = pygame.mouse.get_pos()







        # if event.type == pygame.mouse.get_pressed():
        #     pygame.mouse.get_pressed()
            # length_of_furniture = int(input("enter length of furniture please :3"))
            # width_of_furniture = int(input("enter width of furniture :D"))
            # gitrect.append([length_of_furniture, width_of_furniture])
            # print("HIIIIII")



    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(PURPLE)

    # --- Drawing code should go here
    # pygame.draw.rect(screen,WHITE,(250, 150, length_of_room, width_of_room), 0)
    for elem in gitrect:
        pygame.draw.rect(screen, elem[0], (350, 250, elem[1], elem[2]))
        print(elem)

    # for elem in gitrect:
    #     pygame.draw.rect(screen, GREEN, (350, 250), elem[0], elem[1])
    #     gitrect([pygame.draw.rect(screen, GREEN, (350, 250) )])


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
