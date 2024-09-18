
# * we should ALWAYS import pygame and initialize it. 
import pygame
pygame.init()

# * the line below sets the size of the window
window = pygame.display.set_mode((500, 500))

# * the line below titles the game ont he window displayed.
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60 
vel = 5

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
    
    # * first parameter that gets taken will always be the WINDOW
        #   - everything in pygame is a surface. 
                #  - so  when we create the circle  we create a surface (the circle)
                #  which gets placed onto the window
    # * second parameter is the COLOR (RGB Color)
    # * third, it takes a RECT. 
    # ! depending on whether its a rect or another shape, it require 
    # something other than a rect like a radius for circles
    pygame.draw.rect(window, (128,0,0), (x, y, width, height))
    pygame.display.update()


# Quit the game properly
pygame.quit()
