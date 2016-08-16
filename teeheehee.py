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
COLOR = (170, 255, 128)



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
length_of_room = int(input("Enter length of room"))
width_of_room = int(input("Enter width of room"))

laRect = pygame.Rect(600, 0, 100, 50)

gitrect = []
click = False
drawNew = False
newRect=pygame.Rect(100,100,100,100)
toDrop = False




def random_color():
    return random.choice(colors)
# def holding():
#     global held, coordinates
#     if held:
#         coordinates = pygame.mouse.get_pos()

def make_furniture():
    length_of_furniture = int(input("enter length of furniture"))
    width_of_furniture = int(input("enter width of furniture"))
    newRect = pygame.Rect(100, 100, width_of_furniture, length_of_furniture)
    gitrect.append(newRect)
    print("gitrect: " + str(len(gitrect)))

def follow_mouse(index):
    (mouseX, mouseY) = pygame.mouse.get_pos()
    # newRect = pygame.Rect(mouseX, mouseY, width_of_furniture, length_of_furniture)
    gitrect[index].x = mouseX
    gitrect[index].y = mouseY

def check_furniture_click(mouseX, mouseY):
    for num in range(len(gitrect)):
        print("checking furniture")
        if gitrect[num].collidepoint(mouseX, mouseY) == True:
            return num
    return -1




# length_of_room = int(input("Enter length of room"))
# width_of_room = int(input("Enter width of room"))

# laRect = pygame.Rect(600, 0, 100, 50)

# gitrect = []
# click = False
# drawNew = False
# newRect=pygame.Rect(100,100,100,100)
# toDrop = False
# -------- Main Program Loop -----------

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  


        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if laRect.collidepoint(pygame.mouse.get_pos()) == True:
                print("HIIIIIII")
                make_furniture()
                
                    

            else: 
                numFurniture = check_furniture_click(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

                print(numFurniture)
                if numFurniture != -1:



                    toDrop = not toDrop
                    print(toDrop)
    if toDrop == True:
        follow_mouse(numFurniture)



                

            
                    # if event.type == pygame.MOUSEBUTTONDOWN:
                    #     (mouseX, mouseY) = pygame.mouse.get_pos()
                    #     newRect = pygame.Rect(mouseX, mouseY, width_of_furniture, length_of_furniture)
                    #     click = True
                    #     drawNew = True
                # if check_furniture_click(pygame.mouse.get_pos()) and toDrop == True:
                #     toDrop = False




                    # for elem in gitrect:
                    #     if elem.collidepoint(pygame.mouse.get_pos()) == True:
                    #         toDrop = True
                    #         if toDrop ==True:
                    #             if event.type == pygame.MOUSEBUTTONDOWN:
                    #                 (mouseX, mouseY) = pygame.mouse.get_pos()
                                    # print (mouseX, mouseY)
                                    # click = True
                                    # newRect = pygame.Rect(mouseX, mouseY, width_of_furniture, length_of_furniture)
                                    # drawNew = True
                                    # toDrop = True

                                
    # for elem in gitrect:
        
    #     print(elem)
    #     # print(len(gitrect))
    #     if click == True:
    #         print("TUNA!!")
    #         newRect.x = pygame.mouse.get_pos()[0]
    #         newRect.y = pygame.mouse.get_pos()[1]
    #         # print(newRect.x)
    #         # print(newRect.y)
    #         if toDrop == True:
        
    #             print("HI THERE")
    #             click = False
    #             toDrop = False
    #             drawNew = False


    


    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
   
    screen.fill(PURPLE)


    
    pygame.draw.rect(screen, RED, laRect)

    
    
    # --- Drawing code should go here


    for elem in gitrect:
        pygame.draw.rect(screen, COLOR, elem)

    myfont = pygame.font.SysFont("monospace", 12)

    label = myfont.render("Add Furniture", 1, (255, 255, 0))
    screen.blit(label, (605,15))
        # print(len(gitrect))
    # pygame.draw.rect(screen, BLUE, newRect)



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
