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
  # Выбрать шрифт для использования.
  # Стандартный шрифт, размером в 25.
  font = pygame.font.Font (None, 25)

  # Воспроизвести текст. "True" означает,
  # что текст будет сглаженным (anti-aliased).
  # Чёрный - цвет. Переменную BLACK мы задали ранее,
  # списком [0, 0, 0]
  # Заметьте: эта строка создаёт картинку с буквами,
  # но пока не выводит её на экран.
  text = font.render ("My text", True, BLACK)

  # Вывести сделанную картинку на экран в точке (250, 250)
  screen.blit (text, [250, 250])

  # --- Go ahead and update the screen with what we-ve drawn.
  pygame.display.flip ()

  # --- Limit to 60 frames per second
  clock.tick (60)

# Close the window and quit.
pygame.quit ()
