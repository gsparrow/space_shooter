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

class my_sprite:
  def __init__(self, x, y, velocity_x, velocity_y, size_multiplier):
    self.my_x = x
    self.my_y = y
    self.my_velocity_x = velocity_x
    self.my_velocity_y = velocity_y
    self.size = size_multiplier

  def get_x (self):
    return self.my_x
  def get_y (self):
    return self.my_x
  def get_velocity_x (self):
    return self.my_velocity_x
  def get_velocity_y (self):
    return self.my_velocity_y
  def get_size_multiplier (self):
    return self.size

  def set_x (self, x):
    self.my_x = x
  def set_y (self, y):
    self.my_y = y
  def set_velocity_x (self, velocity_x):
    self.my_velocity_x = velocity_x
  def set_velocity_y (self, velocity_y):
    self.my_velocity_y = velocity_y
  def set_size_multiplier (self, size):
    self.size = size

class space_invader (my_sprite): 
  def __init__(self, x, y, velocity_x, velocity_y, size_multiplier, color):
    my_sprite.__init__(self, x, y, velocity_x, velocity_y, size_multiplier)
    self.change = 1
    self.primary_color = color

  def get_primary_color (self):
    return self.primary_color

  def set_primary_color (self, color):
    self.primary_color = color

  def draw(self):
    self.change = self.change +1
    if self.change%2 == 0:
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  4*self.size,  self.my_y,                 2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x + 16*self.size,  self.my_y,                 2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  6*self.size,  self.my_y +  2*self.size,  2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x + 14*self.size,  self.my_y +  2*self.size,  2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  4*self.size,  self.my_y +  4*self.size, 14*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  2*self.size,  self.my_y +  6*self.size,  4*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  8*self.size,  self.my_y +  6*self.size,  6*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x + 16*self.size,  self.my_y +  6*self.size,  4*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  0*self.size,  self.my_y +  8*self.size, 22*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  0*self.size,  self.my_y + 10*self.size,  2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  4*self.size,  self.my_y + 10*self.size, 14*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x + 20*self.size,  self.my_y + 10*self.size,  2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  0*self.size,  self.my_y + 12*self.size,  2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  4*self.size,  self.my_y + 12*self.size,  2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x + 16*self.size,  self.my_y + 12*self.size,  2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x + 20*self.size,  self.my_y + 12*self.size,  2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  6*self.size,  self.my_y + 14*self.size,  4*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x + 12*self.size,  self.my_y + 14*self.size,  4*self.size, 2*self.size])
    else:
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  4*self.size,  self.my_y,                 2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x + 16*self.size,  self.my_y,                 2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  0*self.size,  self.my_y +  2*self.size,  2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  6*self.size,  self.my_y +  2*self.size,  2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x + 14*self.size,  self.my_y +  2*self.size,  2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x + 20*self.size,  self.my_y +  2*self.size,  2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  0*self.size,  self.my_y +  4*self.size,  2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  4*self.size,  self.my_y +  4*self.size, 14*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x + 20*self.size,  self.my_y +  4*self.size,  2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  0*self.size,  self.my_y +  6*self.size,  6*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  8*self.size,  self.my_y +  6*self.size,  6*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x + 16*self.size,  self.my_y +  6*self.size,  6*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  0*self.size,  self.my_y +  8*self.size, 22*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  2*self.size,  self.my_y + 10*self.size, 18*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  4*self.size,  self.my_y + 12*self.size,  2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x + 16*self.size,  self.my_y + 12*self.size,  2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x +  2*self.size,  self.my_y + 14*self.size,  2*self.size, 2*self.size])
      pygame.draw.rect(screen, self.primary_color, [self.my_x + 18*self.size,  self.my_y + 14*self.size,  2*self.size, 2*self.size])
    
  def move (self):
    if (self.my_x +self.my_velocity_x +22*self.size > WIDTH):
      self.my_velocity_x = -1 * self.my_velocity_x
    elif (self.my_x +self.my_velocity_x < 0):
      self.my_velocity_x = -1 * self.my_velocity_x
    self.my_x += self.my_velocity_x
    if (self.my_y +self.my_velocity_y +16*self.size > HEIGHT):
      self.my_velocity_y = -1 * self.my_velocity_y
    elif (self.my_y +self.my_velocity_y < 0):
      self.my_velocity_y = -1 * self.my_velocity_y
    self.my_y += self.my_velocity_y
    

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Space Invaders")

done = False
clock = pygame.time.Clock()

baddie = space_invader(10,10,2,1,4, RED)

while not done:

  #limit the clock to ten loops per second
  clock.tick(3)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done =True

  screen.fill(BLACK)

  baddie.draw()
  baddie.move()

  pygame.display.flip()

pygame.quit()
