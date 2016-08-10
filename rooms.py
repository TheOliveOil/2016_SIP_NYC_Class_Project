import pygame


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (152, 251, 152)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)
PURPLE =  (160, 32, 240)

pygame.init()

 # Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Room Floorplan")

# Loop until the user clicks the close button.
done = False

# WRITE YOUR CODE HERE
length_of_room = int(input("Enter length of room"))
width_of_room = int(input("Enter width of room"))
hannah = int(input("favorite number, please?"))

# -------- Main Program Loop -----------
while not done:
# 	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.quit:
			done = True
		if event.type == pygame.MOUSEBUTTONDOWN:
			(mouseX, mouseY) = pygame.mouse.get_pos()
			print (mouseX, mouseY)

# def findParticle(particles, x, y):
#     for p in particles:
#         if math.hypot(p.x-x, p.y-y) <= p.size:
#             return p
#     return None




 

	screen.fill(WHITE)

    # --- Drawing code should go here
    # xpoint, ypoint, width, height

	pygame.draw.rect(screen, GREY, (20, 20, width_of_room, length_of_room) , 0)

	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE