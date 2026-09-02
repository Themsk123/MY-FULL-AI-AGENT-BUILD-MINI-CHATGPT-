import pygame
from constants import (
    WIDTH, HEIGHT, BLOCK_SIZE, 
    BLACK, WHITE, GREEN, DARK_GREEN, RED, GRAY, TRANSPARENT_BLACK
)

def draw_grid(screen):
    """Draws background grid lines."""
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

def draw_food(screen, food):
    """Draws the food block."""
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE), border_radius=4)

def draw_snake(screen, snake):
    """Draws the snake body segments."""
    for i, segment in enumerate(snake):
        color = DARK_GREEN if i == 0 else GREEN
        pygame.draw.rect(screen, color, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE), border_radius=4)

def draw_score(screen, font, score):
    """Draws the current score on the screen."""
    score_surface = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surface, (10, 10))

def draw_game_over(screen, font_large, font_small, score):
    """Draws the Game Over overlay and menu."""
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill(TRANSPARENT_BLACK)
    screen.blit(overlay, (0, 0))

    over_surf = font_large.render("GAME OVER", True, RED)
    score_surf = font_small.render(f"Final Score: {score}", True, WHITE)
    restart_surf = font_small.render("Press 'R' to Restart or 'Q' to Quit", True, WHITE)

    screen.blit(over_surf, (WIDTH//2 - over_surf.get_width()//2, HEIGHT//2 - 60))
    screen.blit(score_surf, (WIDTH//2 - score_surf.get_width()//2, HEIGHT//2 - 15))
    screen.blit(restart_surf, (WIDTH//2 - restart_surf.get_width()//2, HEIGHT//2 + 25))
