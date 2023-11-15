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


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 7
        self.image = pygame.Surface((5, 10))
        self.image.fill(WHITE)

    def move(self):
        self.y -= self.speed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


def main_menu():
    while True:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 74)
        title_text = font.render("Space Invaders", True, WHITE)
        title_rect = title_text.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
        )
        screen.blit(title_text, title_rect)

        play_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)
        pygame.draw.rect(screen, GREEN, play_button)

        play_text = font.render("Play", True, WHITE)
        play_rect = play_text.get_rect(center=play_button.center)
        screen.blit(play_text, play_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    return


def show_game_over_message():
    font = pygame.font.Font(None, 74)
    text = font.render("GAME OVER", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
    screen.blit(text, text_rect)


def show_victory_message():
    font = pygame.font.Font(None, 74)
    text = font.render("YOU WIN!", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
    screen.blit(text, text_rect)


def game_over_screen():
    while True:
        show_game_over_message()

        replay_button = pygame.Rect(
            SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100, 200, 50
        )
        pygame.draw.rect(screen, GREEN, replay_button)

        font = pygame.font.Font(None, 50)
        replay_text = font.render("Replay", True, WHITE)
        replay_rect = replay_text.get_rect(center=replay_button.center)
        screen.blit(replay_text, replay_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if replay_button.collidepoint(event.pos):
                    return


def next_round_screen():
    while True:
        show_victory_message()

        next_round_button = pygame.Rect(
            SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 150, 200, 50
        )
        pygame.draw.rect(screen, GREEN, next_round_button)

        font = pygame.font.Font(None, 50)
        next_round_text = font.render("Next Round", True, WHITE)
        next_round_rect = next_round_text.get_rect(center=next_round_button.center)
        screen.blit(next_round_text, next_round_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_round_button.collidepoint(event.pos):
                    return


pygame.quit()
