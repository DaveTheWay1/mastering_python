
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
    # ! without the time delay, it will move insanley fast
    pygame.time.delay(100)
    for event in pygame.event.get():
        # Check if the close button is pressed
        if event.type == pygame.QUIT:
            run = False
    
    # * set up a list
    keys = pygame.key.get_pressed()

    # * to check what key has been pressed
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    
    # ! WITHOUT this line below, instead of moving as expected, it will create a trail from
    # where you started in location to where you move to
    # * the color goes here. in this case, we have it as back
    window.fill((0,0,0))
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
