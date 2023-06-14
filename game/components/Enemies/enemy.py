import random 
from game.utils.constants import SCREEN_WIDTH

class Enemy:
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 1
    LEFT = "left"
    RIGHT = "right"
    MOVE_X = [LEFT, RIGHT]
    INTERVAL = 100





    def __init__(self, image):
          self.image = image
          self.rect = self.image.get_rect()
          self.rect.x = random.choice(self.X_POS_LIST)
          self.rect.y = self.Y_POS
          self.MOVE_X = random.choice(self.MOVE_X)
          self.index = 0

    
    def update (self):
         self.rect.y += self.SPEED_Y
         if self.MOVE_X == self.LEFT:
              self.rect.x -= self.SPEED_X
              if self.index > self.INTERVAL or self.rect.x <= 0:
                   self.MOVE_X = self.RIGHT
                   self.index = 0
              
         else:
              self.rect.x += self.SPEED_X
              if self.index > self.INTERVAL or self.rect.x >= SCREEN_WIDTH - self.rect.width:
                   self.MOVE_X = self.LEFT
                   self.index = 0
              self.index += 1
    
    def draw(self, screen):
         screen.blit(self.image, self.rect)
         