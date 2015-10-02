#!/usr/bin/python

import sys
import pygame
import sprites

pygame.init()
WIDTH = 320
HEIGHT = 240
size = WIDTH, HEIGHT
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

    
    

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Space Invaders")

done = False
clock = pygame.time.Clock()

baddie  = sprites.space_invader_squid(  0, 0, 0, 0, 4, WHITE, screen)
baddie2 = sprites.space_invader_crab ( 80, 0, 0, 0, 4, WHITE, screen)
baddie3 = sprites.space_invader_jellyfish (180, 0, 0, 0, 4, WHITE, screen)
ship = sprites.ship ( 80, 100, 0, 0, 4, WHITE, RED, BLUE, screen)
while not done:

  #limit the clock to ten loops per second
  clock.tick(3)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done =True

  screen.fill(BLACK)

  ship.draw()
  ship.move()
  baddie.draw()
  baddie.move()
  baddie2.draw()
  baddie2.move()
  baddie3.draw()
  baddie3.move()

  pygame.display.flip()

pygame.quit()
