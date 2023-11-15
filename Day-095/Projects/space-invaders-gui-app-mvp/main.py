import sys
import pygame


pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 36, 24
ALIEN_WIDTH, ALIEN_HEIGHT = 36, 24
BULLET_WIDTH, BULLET_HEIGHT = 5, 10
ALIEN_SPACING = 60

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
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(GREEN)

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        elif direction == "right" and self.x < SCREEN_WIDTH - PLAYER_WIDTH:
            self.x += self.speed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class Alien:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = alien_speed
        self.image = pygame.Surface((ALIEN_WIDTH, ALIEN_HEIGHT))
        self.image.fill(RED)

    def move(self):
        self.x += self.speed

    def drop_down(self):
        self.y += ALIEN_HEIGHT

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 7
        self.image = pygame.Surface((BULLET_WIDTH, BULLET_HEIGHT))
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
    screen.fill(RED, text_rect)
    screen.blit(text, text_rect)

    font = pygame.font.Font(None, 50)
    text = font.render("YOU LOSE", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
    screen.fill(RED, text_rect)
    screen.blit(text, text_rect)


def show_victory_message():
    font = pygame.font.Font(None, 74)
    text = font.render("GAME OVER", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 - 40))
    screen.fill(GREEN, text_rect)
    screen.blit(text, text_rect)

    font = pygame.font.Font(None, 50)
    text = font.render("YOU WIN!", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + 20))
    screen.fill(GREEN, text_rect)
    screen.blit(text, text_rect)

    font = pygame.font.Font(None, 50)
    round_text = font.render(f"ROUND {current_round}/3", True, WHITE)
    round_rect = round_text.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3 + 60)
    )
    screen.fill(GREEN, round_rect)
    screen.blit(round_text, round_rect)


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
    global current_round, alien_speed

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
                    if current_round < 3:
                        current_round += 1
                        alien_speed += 0.25
                        return


def game_loop():
    player = Player()
    aliens = [Alien(x * ALIEN_SPACING, y * 50) for x in range(10) for y in range(3)]
    bullets = []
    bullet_active = False
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill((0, 0, 0))
        edge_hit = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not bullet_active:
                    bullets.append(Bullet(player.x + PLAYER_WIDTH // 2, player.y))
                    bullet_active = True

        for alien in aliens:
            alien.move()
            if alien.x <= 0 or alien.x >= SCREEN_WIDTH - ALIEN_WIDTH:
                edge_hit = True
            if alien.y + ALIEN_HEIGHT >= player.y:
                game_over_screen()
                pygame.display.flip()
                pygame.time.wait(3000)
                running = False
                return

        if edge_hit:
            for alien in aliens:
                alien.drop_down()
                alien.speed *= -1

        if not aliens:
            next_round_screen()
            show_victory_message()
            pygame.display.flip()
            pygame.time.wait(3000)
            return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move("left")
        if keys[pygame.K_RIGHT]:
            player.move("right")

        for alien in aliens:
            alien.move()
            alien.draw()

        for bullet in bullets[:]:
            bullet.move()
            bullet.draw()
            if bullet.y < 0:
                bullets.remove(bullet)
                bullet_active = False

        for bullet in bullets:
            for alien in aliens:
                if (
                    alien.x < bullet.x < alien.x + ALIEN_WIDTH
                    and alien.y < bullet.y < alien.y + ALIEN_HEIGHT
                ):
                    aliens.remove(alien)
                    bullets.remove(bullet)
                    bullet_active = False
                    break

        font = pygame.font.Font(None, 36)
        round_text = font.render(f"Round {current_round}/3", True, WHITE)
        screen.blit(round_text, (SCREEN_WIDTH - 150, 10))

        player.draw()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


main_menu()
current_round = 1
alien_speed = 0.5

while True:
    while current_round <= 3:
        game_loop()
        if current_round > 3:
            break
    current_round = 1
    alien_speed = 0.5
    main_menu()
