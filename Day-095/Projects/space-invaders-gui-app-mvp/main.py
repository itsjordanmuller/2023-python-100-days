import sys
import pygame


pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders MVP")


class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - 60
        self.speed = 5
        self.image = pygame.Surface((36, 24))
        self.image.fill(GREEN)

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        elif direction == "right" and self.x < SCREEN_WIDTH - 36:
            self.x += self.speed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class Alien:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0.5
        self.image = pygame.Surface((36, 24))
        self.image.fill(RED)

    def move(self):
        self.x += self.speed

    def drop_down(self):
        self.y += 24

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


pygame.quit()
