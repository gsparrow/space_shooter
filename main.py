#!/usr/bin/python

import sys
import pygame
import sprites

pygame.init()
WIDTH = 640
HEIGHT = 480
size = WIDTH, HEIGHT
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
ORANGE= (255, 165,   0)
    
    

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Space Invaders")

done = False
clock = pygame.time.Clock()

baddie  = sprites.Flower(  0, 0, 0, 0, 4, WHITE, ORANGE, GREEN, screen)
baddie2 = sprites.space_invader_crab ( 160, 0, 0, 0, 4, WHITE, screen)
baddie3 = sprites.space_invader_squid (360, 0, 0, 0, 4, WHITE, screen)
baddie4 = sprites.space_invader_jellyfish (200, 100, 0, 0, 4, WHITE, screen)
ship = sprites.ship ( 0, 100, 0, 0, 4, WHITE, RED, BLUE, screen)
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
  baddie4.draw()
  baddie4.move()

  pygame.display.flip()

pygame.quit()
