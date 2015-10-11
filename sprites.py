import pygame

class my_sprite:
  def __init__(self, x, y, velocity_x, velocity_y, size_multiplier):
    self.my_x = x
    self.my_y = y
    self.my_velocity_x = velocity_x
    self.my_velocity_y = velocity_y
    if size_multiplier < 2:
      self.size = 2
    else:
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

class space_invader_crab (my_sprite): 
  def __init__(self, x, y, velocity_x, velocity_y, size_multiplier, color, screen):
    my_sprite.__init__(self, x, y, velocity_x, velocity_y, size_multiplier)
    self.change = 1
    self.primary_color = color
    self.screen = screen

  def get_primary_color (self):
    return self.primary_color

  def set_primary_color (self, color):
    self.primary_color = color

  def draw(self):
    self.change = self.change +1
    if self.change%2 == 0:
      self.draw_left()
    else:
      self.draw_right()

  def draw_left(self):
    #draw a rectangle (on the screen, of color, [starting at base x plus block position times block size multiplier, same for y, 
      #of length number of blocks times block size multiplier, same for y]
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  2*self.size,  self.my_y + 0*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  8*self.size,  self.my_y + 0*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  3*self.size,  self.my_y + 1*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  7*self.size,  self.my_y + 1*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  2*self.size,  self.my_y + 2*self.size,  7*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  1*self.size,  self.my_y + 3*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  4*self.size,  self.my_y + 3*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  8*self.size,  self.my_y + 3*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  0*self.size,  self.my_y + 4*self.size, 11*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  0*self.size,  self.my_y + 5*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  2*self.size,  self.my_y + 5*self.size,  7*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 10*self.size,  self.my_y + 5*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  0*self.size,  self.my_y + 6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  2*self.size,  self.my_y + 6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  8*self.size,  self.my_y + 6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 10*self.size,  self.my_y + 6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  3*self.size,  self.my_y + 7*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  6*self.size,  self.my_y + 7*self.size,  2*self.size, 1*self.size])

  def draw_right(self):
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  2*self.size,  self.my_y + 0*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  8*self.size,  self.my_y + 0*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  0*self.size,  self.my_y + 1*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  3*self.size,  self.my_y + 1*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  7*self.size,  self.my_y + 1*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 10*self.size,  self.my_y + 1*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  0*self.size,  self.my_y + 2*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  2*self.size,  self.my_y + 2*self.size,  7*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 10*self.size,  self.my_y + 2*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  0*self.size,  self.my_y + 3*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  4*self.size,  self.my_y + 3*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  8*self.size,  self.my_y + 3*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  0*self.size,  self.my_y + 4*self.size, 11*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  1*self.size,  self.my_y + 5*self.size,  9*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  2*self.size,  self.my_y + 6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  8*self.size,  self.my_y + 6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  1*self.size,  self.my_y + 7*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  9*self.size,  self.my_y + 7*self.size,  1*self.size, 1*self.size])

  def move (self):
    if (self.my_x +self.my_velocity_x +22*self.size > self.screen.get_width()):
      self.my_velocity_x = -1 * self.my_velocity_x
    elif (self.my_x +self.my_velocity_x < 0):
      self.my_velocity_x = -1 * self.my_velocity_x
    self.my_x += self.my_velocity_x
    if (self.my_y +self.my_velocity_y +16*self.size > self.screen.get_height()):
      self.my_velocity_y = -1 * self.my_velocity_y
    elif (self.my_y +self.my_velocity_y < 0):
      self.my_velocity_y = -1 * self.my_velocity_y
    self.my_y += self.my_velocity_y

class space_invader_squid (my_sprite): 
  def __init__(self, x, y, velocity_x, velocity_y, size_multiplier, color, screen):
    my_sprite.__init__(self, x, y, velocity_x, velocity_y, size_multiplier)
    self.change = 1
    self.primary_color = color
    self.screen = screen

  def get_primary_color (self):
    return self.primary_color

  def set_primary_color (self, color):
    self.primary_color = color

  def draw(self):
    self.change = self.change +1
    if self.change%2 == 0:
      self.draw_left()
    else:
      self.draw_right()

  def draw_left(self):
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 3*self.size,  self.my_y + 0*self.size, 2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 2*self.size,  self.my_y + 1*self.size, 4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 1*self.size,  self.my_y + 2*self.size, 6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 0*self.size,  self.my_y + 3*self.size, 2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 3*self.size,  self.my_y + 3*self.size, 2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 6*self.size,  self.my_y + 3*self.size, 2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 0*self.size,  self.my_y + 4*self.size, 8*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 2*self.size,  self.my_y + 5*self.size, 1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 5*self.size,  self.my_y + 5*self.size, 1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 1*self.size,  self.my_y + 6*self.size, 1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 3*self.size,  self.my_y + 6*self.size, 2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 6*self.size,  self.my_y + 6*self.size, 1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 0*self.size,  self.my_y + 7*self.size, 1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 2*self.size,  self.my_y + 7*self.size, 1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 5*self.size,  self.my_y + 7*self.size, 1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 7*self.size,  self.my_y + 7*self.size, 1*self.size, 1*self.size])

  def draw_right(self):
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 3*self.size,  self.my_y + 0*self.size, 2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 2*self.size,  self.my_y + 1*self.size, 4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 1*self.size,  self.my_y + 2*self.size, 6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 0*self.size,  self.my_y + 3*self.size, 2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 3*self.size,  self.my_y + 3*self.size, 2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 6*self.size,  self.my_y + 3*self.size, 2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 0*self.size,  self.my_y + 4*self.size, 8*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 1*self.size,  self.my_y + 5*self.size, 1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 3*self.size,  self.my_y + 5*self.size, 2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 6*self.size,  self.my_y + 5*self.size, 1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 0*self.size,  self.my_y + 6*self.size, 1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 7*self.size,  self.my_y + 6*self.size, 1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 1*self.size,  self.my_y + 7*self.size, 1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 6*self.size,  self.my_y + 7*self.size, 1*self.size, 1*self.size])

  def move (self):
    if (self.my_x +self.my_velocity_x +16*self.size > self.screen.get_width()):
      self.my_velocity_x = -1 * self.my_velocity_x
    elif (self.my_x +self.my_velocity_x < 0):
      self.my_velocity_x = -1 * self.my_velocity_x
    self.my_x += self.my_velocity_x
    if (self.my_y +self.my_velocity_y +16*self.size > self.screen.get_height()):
      self.my_velocity_y = -1 * self.my_velocity_y
    elif (self.my_y +self.my_velocity_y < 0):
      self.my_velocity_y = -1 * self.my_velocity_y
    self.my_y += self.my_velocity_y

class space_invader_jellyfish (my_sprite): 
  def __init__(self, x, y, velocity_x, velocity_y, size_multiplier, color, screen):
    my_sprite.__init__(self, x, y, velocity_x, velocity_y, size_multiplier)
    self.change = 1
    self.primary_color = color
    self.screen = screen

  def get_primary_color (self):
    return self.primary_color

  def set_primary_color (self, color):
    self.primary_color = color

  def draw(self):
    self.change = self.change +1
    if self.change%2 == 0:
      self.draw_left()
    else:
      self.draw_right()

  def draw_left(self):
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 4*self.size,  self.my_y + 0*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 1*self.size,  self.my_y + 1*self.size, 10*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 0*self.size,  self.my_y + 2*self.size, 12*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 0*self.size,  self.my_y + 3*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 5*self.size,  self.my_y + 3*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 9*self.size,  self.my_y + 3*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 0*self.size,  self.my_y + 4*self.size, 12*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 2*self.size,  self.my_y + 5*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 7*self.size,  self.my_y + 5*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 1*self.size,  self.my_y + 6*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 5*self.size,  self.my_y + 6*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 9*self.size,  self.my_y + 6*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 2*self.size,  self.my_y + 7*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 8*self.size,  self.my_y + 7*self.size,  2*self.size, 1*self.size])

  def draw_right(self):
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  4*self.size,  self.my_y + 0*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  1*self.size,  self.my_y + 1*self.size, 10*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  0*self.size,  self.my_y + 2*self.size, 12*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  0*self.size,  self.my_y + 3*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  5*self.size,  self.my_y + 3*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  9*self.size,  self.my_y + 3*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  0*self.size,  self.my_y + 4*self.size, 12*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  3*self.size,  self.my_y + 5*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  7*self.size,  self.my_y + 5*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  2*self.size,  self.my_y + 6*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  5*self.size,  self.my_y + 6*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  8*self.size,  self.my_y + 6*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x +  0*self.size,  self.my_y + 7*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color, [self.my_x + 10*self.size,  self.my_y + 7*self.size,  2*self.size, 1*self.size])

  def move (self):
    if (self.my_x +self.my_velocity_x +26*self.size > self.screen.get_width()):
      self.my_velocity_x = -1 * self.my_velocity_x
    elif (self.my_x +self.my_velocity_x < 0):
      self.my_velocity_x = -1 * self.my_velocity_x
    self.my_x += self.my_velocity_x
    if (self.my_y +self.my_velocity_y +16*self.size > self.screen.get_height()):
      self.my_velocity_y = -1 * self.my_velocity_y
    elif (self.my_y +self.my_velocity_y < 0):
      self.my_velocity_y = -1 * self.my_velocity_y
    self.my_y += self.my_velocity_y

class ship (my_sprite): 
  def __init__(self, x, y, velocity_x, velocity_y, size_multiplier, color, color2, color3, screen):
    my_sprite.__init__(self, x, y, velocity_x, velocity_y, size_multiplier)
    self.primary_color   = color
    self.secondary_color = color2
    self.tertiary_color  = color3
    self.screen          = screen

  def get_primary_color (self):
    return self.primary_color

  def set_primary_color (self, color):
    self.primary_color = color

  def draw(self):
      pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  0*self.size,  self.my_y +  7*self.size, 1*self.size, 2*self.size])
      pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  0*self.size,  self.my_y +  9*self.size, 1*self.size, 7*self.size])
      pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  1*self.size,  self.my_y + 12*self.size, 1*self.size, 3*self.size])
      pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  2*self.size,  self.my_y + 11*self.size, 1*self.size, 3*self.size])
      pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  3*self.size,  self.my_y +  5*self.size, 1*self.size, 2*self.size])
      pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  3*self.size,  self.my_y +  7*self.size, 1*self.size, 2*self.size])
      pygame.draw.rect(self.screen, self.tertiary_color,  [self.my_x +  3*self.size,  self.my_y +  9*self.size, 1*self.size, 1*self.size])
      pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  3*self.size,  self.my_y + 10*self.size, 1*self.size, 3*self.size])
      pygame.draw.rect(self.screen, self.tertiary_color,  [self.my_x +  4*self.size,  self.my_y +  8*self.size, 1*self.size, 1*self.size])
      pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  4*self.size,  self.my_y +  9*self.size, 1*self.size, 4*self.size])
      pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  4*self.size,  self.my_y + 13*self.size, 1*self.size, 2*self.size])
      pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  5*self.size,  self.my_y +  7*self.size, 1*self.size, 5*self.size])
      pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  5*self.size,  self.my_y + 12*self.size, 1*self.size, 3*self.size])
      pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  6*self.size,  self.my_y +  3*self.size, 1*self.size, 6*self.size])
      pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  6*self.size,  self.my_y +  9*self.size, 1*self.size, 2*self.size])
      pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  6*self.size,  self.my_y + 11*self.size, 1*self.size, 3*self.size])
      pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  7*self.size,  self.my_y +  0*self.size, 1*self.size, 8*self.size])
      pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  7*self.size,  self.my_y +  8*self.size, 1*self.size, 2*self.size])
      pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  7*self.size,  self.my_y + 10*self.size, 1*self.size, 6*self.size])
      pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  8*self.size,  self.my_y +  3*self.size, 1*self.size, 6*self.size])
      pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  8*self.size,  self.my_y +  9*self.size, 1*self.size, 2*self.size])
      pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  8*self.size,  self.my_y + 11*self.size, 1*self.size, 3*self.size])
      pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  9*self.size,  self.my_y +  7*self.size, 1*self.size, 5*self.size])
      pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  9*self.size,  self.my_y + 12*self.size, 1*self.size, 3*self.size])
      pygame.draw.rect(self.screen, self.tertiary_color,  [self.my_x + 10*self.size,  self.my_y +  8*self.size, 1*self.size, 1*self.size])
      pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 10*self.size,  self.my_y +  9*self.size, 1*self.size, 4*self.size])
      pygame.draw.rect(self.screen, self.secondary_color, [self.my_x + 10*self.size,  self.my_y + 13*self.size, 1*self.size, 2*self.size])
      pygame.draw.rect(self.screen, self.secondary_color, [self.my_x + 11*self.size,  self.my_y +  5*self.size, 1*self.size, 2*self.size])
      pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 11*self.size,  self.my_y +  7*self.size, 1*self.size, 2*self.size])
      pygame.draw.rect(self.screen, self.tertiary_color,  [self.my_x + 11*self.size,  self.my_y +  9*self.size, 1*self.size, 1*self.size])
      pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 11*self.size,  self.my_y + 10*self.size, 1*self.size, 3*self.size])
      pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 12*self.size,  self.my_y + 11*self.size, 1*self.size, 3*self.size])
      pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 13*self.size,  self.my_y + 12*self.size, 1*self.size, 3*self.size])
      pygame.draw.rect(self.screen, self.secondary_color, [self.my_x + 14*self.size,  self.my_y +  7*self.size, 1*self.size, 2*self.size])
      pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 14*self.size,  self.my_y +  9*self.size, 1*self.size, 7*self.size])

  def move (self):
    if (self.my_x +self.my_velocity_x +30*self.size > self.screen.get_width()):
      self.my_velocity_x = -1 * self.my_velocity_x
    elif (self.my_x +self.my_velocity_x < 0):
      self.my_velocity_x = -1 * self.my_velocity_x
    self.my_x += self.my_velocity_x
    if (self.my_y +self.my_velocity_y +30*self.size > self.screen.get_height()):
      self.my_velocity_y = -1 * self.my_velocity_y
    elif (self.my_y +self.my_velocity_y < 0):
      self.my_velocity_y = -1 * self.my_velocity_y
    self.my_y += self.my_velocity_y


class Flower (my_sprite): 
  def __init__(self, x, y, velocity_x, velocity_y, size_multiplier, color, color2, color3, screen):
    my_sprite.__init__(self, x, y, velocity_x, velocity_y, size_multiplier)
    self.primary_color   = color
    self.secondary_color = color2
    self.tertiary_color  = color3
    self.screen          = screen

  def get_primary_color (self):
    return self.primary_color

  def set_primary_color (self, color):
    self.primary_color = color

  def draw(self):
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  7*self.size,  self.my_y +  0*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  2*self.size,  self.my_y +  1*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  6*self.size,  self.my_y +  1*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  7*self.size,  self.my_y +  1*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  9*self.size,  self.my_y +  1*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 13*self.size,  self.my_y +  1*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  1*self.size,  self.my_y +  2*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  2*self.size,  self.my_y +  2*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  3*self.size,  self.my_y +  2*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  5*self.size,  self.my_y +  2*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  6*self.size,  self.my_y +  2*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 10*self.size,  self.my_y +  2*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 12*self.size,  self.my_y +  2*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.secondary_color, [self.my_x + 13*self.size,  self.my_y +  2*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 14*self.size,  self.my_y +  2*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  1*self.size,  self.my_y +  3*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  2*self.size,  self.my_y +  3*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  4*self.size,  self.my_y +  3*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  5*self.size,  self.my_y +  3*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 11*self.size,  self.my_y +  3*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.secondary_color, [self.my_x + 12*self.size,  self.my_y +  3*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 14*self.size,  self.my_y +  3*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  0*self.size,  self.my_y +  4*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  1*self.size,  self.my_y +  4*self.size, 14*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 15*self.size,  self.my_y +  4*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  0*self.size,  self.my_y +  5*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  1*self.size,  self.my_y +  5*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  4*self.size,  self.my_y +  5*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  6*self.size,  self.my_y +  5*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  9*self.size,  self.my_y +  5*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.secondary_color, [self.my_x + 11*self.size,  self.my_y +  5*self.size,  4*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 15*self.size,  self.my_y +  5*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  0*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  1*self.size,  self.my_y +  6*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  3*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  4*self.size,  self.my_y +  6*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  6*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  7*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  8*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  9*self.size,  self.my_y +  6*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 11*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.secondary_color, [self.my_x + 12*self.size,  self.my_y +  6*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 15*self.size,  self.my_y +  6*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  0*self.size,  self.my_y +  7*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  1*self.size,  self.my_y +  7*self.size, 14*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 15*self.size,  self.my_y +  7*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  1*self.size,  self.my_y +  8*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  2*self.size,  self.my_y +  8*self.size, 12*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 14*self.size,  self.my_y +  8*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  2*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  3*self.size,  self.my_y +  9*self.size, 10*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 13*self.size,  self.my_y +  9*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  3*self.size,  self.my_y + 10*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.secondary_color, [self.my_x +  5*self.size,  self.my_y + 10*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 11*self.size,  self.my_y + 10*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  5*self.size,  self.my_y + 11*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  2*self.size,  self.my_y + 12*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  6*self.size,  self.my_y + 12*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.tertiary_color,  [self.my_x +  7*self.size,  self.my_y + 12*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  9*self.size,  self.my_y + 12*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 11*self.size,  self.my_y + 12*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  1*self.size,  self.my_y + 13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.tertiary_color,  [self.my_x +  2*self.size,  self.my_y + 13*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  5*self.size,  self.my_y + 13*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.tertiary_color,  [self.my_x +  7*self.size,  self.my_y + 13*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  9*self.size,  self.my_y + 13*self.size,  2*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.tertiary_color,  [self.my_x + 11*self.size,  self.my_y + 13*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 14*self.size,  self.my_y + 13*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  0*self.size,  self.my_y + 14*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.tertiary_color,  [self.my_x +  1*self.size,  self.my_y + 14*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  6*self.size,  self.my_y + 14*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.tertiary_color,  [self.my_x +  7*self.size,  self.my_y + 14*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  8*self.size,  self.my_y + 14*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.tertiary_color,  [self.my_x +  9*self.size,  self.my_y + 14*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 15*self.size,  self.my_y + 14*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  0*self.size,  self.my_y + 15*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.tertiary_color,  [self.my_x +  1*self.size,  self.my_y + 15*self.size,  5*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  6*self.size,  self.my_y + 15*self.size,  3*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.tertiary_color,  [self.my_x +  9*self.size,  self.my_y + 15*self.size,  6*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x + 15*self.size,  self.my_y + 15*self.size,  1*self.size, 1*self.size])
    pygame.draw.rect(self.screen, self.primary_color,   [self.my_x +  0*self.size,  self.my_y + 16*self.size, 16*self.size, 1*self.size])


  def move (self):
    if (self.my_x +self.my_velocity_x +30*self.size > self.screen.get_width()):
      self.my_velocity_x = -1 * self.my_velocity_x
    elif (self.my_x +self.my_velocity_x < 0):
      self.my_velocity_x = -1 * self.my_velocity_x
    self.my_x += self.my_velocity_x
    if (self.my_y +self.my_velocity_y +30*self.size > self.screen.get_height()):
      self.my_velocity_y = -1 * self.my_velocity_y
    elif (self.my_y +self.my_velocity_y < 0):
      self.my_velocity_y = -1 * self.my_velocity_y
    self.my_y += self.my_velocity_y
