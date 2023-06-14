from game.components.Enemies.ship import Ship
from game.components.Enemies.ship import Alien

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.enemies.append(Ship())
        self.enemies.append(Alien())

    def update(self):
        for enemy in self.enemies:
             enemy.update()

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)