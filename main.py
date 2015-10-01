#!/usr/bin/python

import sys
import pygame

pygame.init()
WIDTH = 320
HEIGHT = 240
size = WIDTH, HEIGHT
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

class space_invader (object): 
  def __init__(self, x, y, velocity_x, velocity_y, size_multiplier):
    self.my_x = x
    self.my_y = y
    self.my_velocity_x = velocity_x
    self.my_velocity_y = velocity_y
    self.size = size_multiplier

  def draw(self):
    pygame.draw.rect(screen, WHITE, [self.my_x +  4*self.size,  self.my_y,                 2*self.size, 2*self.size])
    pygame.draw.rect(screen, WHITE, [self.my_x + 16*self.size,  self.my_y,                 2*self.size, 2*self.size])
    pygame.draw.rect(screen, WHITE, [self.my_x +  6*self.size,  self.my_y +  2*self.size,  2*self.size, 2*self.size])
    pygame.draw.rect(screen, WHITE, [self.my_x + 14*self.size,  self.my_y +  2*self.size,  2*self.size, 2*self.size])
    pygame.draw.rect(screen, WHITE, [self.my_x +  4*self.size,  self.my_y +  4*self.size, 14*self.size, 2*self.size])
    pygame.draw.rect(screen, WHITE, [self.my_x +  2*self.size,  self.my_y +  6*self.size,  4*self.size, 2*self.size])
    pygame.draw.rect(screen, WHITE, [self.my_x +  8*self.size,  self.my_y +  6*self.size,  6*self.size, 2*self.size])
    pygame.draw.rect(screen, WHITE, [self.my_x + 16*self.size,  self.my_y +  6*self.size,  4*self.size, 2*self.size])
    pygame.draw.rect(screen, WHITE, [self.my_x +  0*self.size,  self.my_y +  8*self.size, 22*self.size, 2*self.size])
    pygame.draw.rect(screen, WHITE, [self.my_x +  0*self.size,  self.my_y + 10*self.size,  2*self.size, 2*self.size])
    pygame.draw.rect(screen, WHITE, [self.my_x +  4*self.size,  self.my_y + 10*self.size, 14*self.size, 2*self.size])
    pygame.draw.rect(screen, WHITE, [self.my_x + 20*self.size,  self.my_y + 10*self.size,  2*self.size, 2*self.size])
    pygame.draw.rect(screen, WHITE, [self.my_x +  0*self.size,  self.my_y + 12*self.size,  2*self.size, 2*self.size])
    pygame.draw.rect(screen, WHITE, [self.my_x +  4*self.size,  self.my_y + 12*self.size,  2*self.size, 2*self.size])
    pygame.draw.rect(screen, WHITE, [self.my_x + 16*self.size,  self.my_y + 12*self.size,  2*self.size, 2*self.size])
    pygame.draw.rect(screen, WHITE, [self.my_x + 20*self.size,  self.my_y + 12*self.size,  2*self.size, 2*self.size])
    pygame.draw.rect(screen, WHITE, [self.my_x +  6*self.size,  self.my_y + 14*self.size,  4*self.size, 2*self.size])
    pygame.draw.rect(screen, WHITE, [self.my_x + 12*self.size,  self.my_y + 14*self.size,  4*self.size, 2*self.size])
    
    
    

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Space Invaders")

done = False
clock = pygame.time.Clock()

baddie = space_invader(10,10,0,0,4)

while not done:

  #limit the clock to ten loops per second
  clock.tick(10)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done =True

  screen.fill(BLACK)

  baddie.draw()

  pygame.display.flip()

pygame.quit()
