
# * we should ALWAYS import pygame and initialize it. 
import pygame
pygame.init()

# * the line below sets the size of the window
window = pygame.display.set_mode((500, 500))

# * the line below titles the game ont he window displayed.
pygame.display.set_caption("First Game")

# * Set up a flag to keep the window open
# without it, the window may close immeidately.
run = True

# * Main game loop
# with this loop, this assures the window stays running
# while run is true. if turned to false, the window will close
while run:
    for event in pygame.event.get():
        # Check if the close button is pressed
        if event.type == pygame.QUIT:
            run = False


# Quit the game properly
pygame.quit()
