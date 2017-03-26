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

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

# -------- Main Program Loop -----------
while not done:
  # --- Main event loop
  for event in pygame.event.get ():
    if event.type == pygame.QUIT:
      done = True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE: done = True

      # Figure out if it was an arrow key. If so
      # adjust speed.
      elif event.key == pygame.K_LEFT:  x_speed = -3
      elif event.key == pygame.K_RIGHT: x_speed =  3
      elif event.key == pygame.K_UP:    y_speed = -3
      elif event.key == pygame.K_DOWN:  y_speed =  3

    # User let up on a key
    elif event.type == pygame.KEYUP:
      # If it is an arrow key, reset vector back to zero
      if   event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: x_speed = 0
      elif event.key == pygame.K_UP   or event.key == pygame.K_DOWN:  y_speed = 0

  # --- Game logic should go here

  # Move the object according to the speed vector.
  x_coord = x_coord + x_speed
  y_coord = y_coord + y_speed

  # --- Screen-cleaning code goes here

  # Here, we clear the screen to white. Don`t put other drawing commands
  # above this, or they will be erased with this command.

  # If you want a background image, replace this clear with blit`ing the
  # background image.
  screen.fill (WHITE)

  # --- Drawing code should go here
  draw_stick_figure (screen, x_coord, y_coord)

  # --- Go ahead and update the screen with what we-ve drawn.
  pygame.display.flip ()

  # --- Limit to 60 frames per second
  clock.tick (60)

# Close the window and quit.
pygame.quit ()
