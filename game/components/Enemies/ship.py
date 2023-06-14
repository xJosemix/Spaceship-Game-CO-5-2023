import pygame

from game.components.Enemies.enemy import Enemy
from game.utils.constants import ENEMY_1
from game.utils.constants import ENEMY_2

class Ship(Enemy):
    WIDTH = 40
    HEIGTH = 60

    def __init__(self):
        self.image = ENEMY_1
        self.image = pygame. transform.scale(self.image, (self.WIDTH, self.HEIGTH))
        super().__init__(self.image, speed_x = 5, speed_y = 1)     

class Alien(Enemy):
    WIDTH = 40
    HEIGHT = 60

    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image, speed_x = 10, speed_y = 5)
