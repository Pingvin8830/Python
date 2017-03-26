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

def draw_stick_figure (screen, x, y):
  # Head
  pygame.draw.ellipse (screen, BLACK, [1 + x, y, 10, 10], 0)

  # Legs
  pygame.draw.line (screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
  pygame.draw.line (screen, BLACK, [5 + x, 17 + y], [     x, 27 + y], 2)

  # Body
  pygame.draw.line (screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)

  # Arms
  pygame.draw.line (screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
  pygame.draw.line (screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

# Setup
pygame.init ()

# Set the width and height of the screen [width, height]
size = [700, 500]
screen = pygame.display.set_mode (size)

pygame.display.set_caption ('My Game')

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock ()

# Hide the mouse cursor
pygame.mouse.set_visible (0)

# -------- Main Program Loop -----------
while not done:
  # --- Main event loop
  # ALL EVENT PROGRESSING SHOULD GO BELOW THIS COMMENT
  for event in pygame.event.get ():
    if event.type == pygame.QUIT:
      done = True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE: done = True
  # ALL EVENT PROGRESSING SHOULD GO ABOVE THIS COMMENT

  # --- Game logic should go here
  # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

  # Call draw stick figure function
  pos = pygame.mouse.get_pos ()
  x = pos [0]
  y = pos [1]
  # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

  # --- Screen-cleaning code goes here

  # Here, we clear the screen to white. Don`t put other drawing commands
  # above this, or they will be erased with this command.

  # If you want a background image, replace this clear with blit`ing the
  # background image.

  # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

  # First, clear the screen to white. Don`t put other drawing commands
  # above this, or they will be erased with this command.
  screen.fill (WHITE)

  # --- Drawing code should go here
  draw_stick_figure (screen, x, y)

  # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

  # --- Go ahead and update the screen with what we-ve drawn.
  pygame.display.flip ()

  # --- Limit to 20 frames per second
  clock.tick (60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
