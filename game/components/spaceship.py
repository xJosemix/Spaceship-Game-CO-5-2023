import pygame
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship():
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.is_alive = True

    def update(self, user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_rigth()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move_left(self):
        self.rect.x -= 10
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH

    def move_rigth(self):
        self.rect.x += 10
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2 :
            self.rect.y -= 10

    def move_down(self):
        if self.rect.y < (SCREEN_HEIGHT) - 60 :
            self.rect.y += 10
