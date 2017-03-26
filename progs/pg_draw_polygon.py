#!/bin/python

'''
  Pygame base tamplate for opening a window

  Sample Python/Pygame Programs
  Simson College Computer Science
  http://programarcadegames.com/
  http://simpson.edu/computer-science/

  Explanation video: http://youtu.bu/vRB_983kUMc
'''

import pygame

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)
PI    = 3.141592653

pygame.init ()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode (size)

pygame.display.set_caption ('My Game')

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock ()

# -------- Main Program Loop -----------
while not done:
  # --- Main event loop
  for event in pygame.event.get ():
    if event.type == pygame.QUIT:
      done = True

  # --- Game logic should go here

  # --- Screen-cleaning code goes here

  # Here, we clear the screen to white. Don`t put other drawing commands
  # above this, or they will be erased with this command.

  # If you want a background image, replace this clear with blit`ing the
  # background image.
  screen.fill (WHITE)

  # --- Drawing code should go here
  # Эта команда рисует треугольник, используя функцию polygon
  pygame.draw.polygon (screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

  # --- Go ahead and update the screen with what we-ve drawn.
  pygame.display.flip ()

  # --- Limit to 60 frames per second
  clock.tick (60)

# Close the window and quit.
pygame.quit ()
