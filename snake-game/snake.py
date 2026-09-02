import sys
import pygame
from constants import WIDTH, HEIGHT, FPS
from game_logic import reset_game, spawn_food, update_snake_position, check_collisions
from renderer import draw_grid, draw_food, draw_snake, draw_score, draw_game_over

def main():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Modular Snake Game - Sahil's Edition")
    clock = pygame.time.Clock()

    # Fonts
    font_small = pygame.font.SysFont("arial", 20)
    font_large = pygame.font.SysFont("arial", 36)

    # Game state initialization
    snake, direction, next_direction, food, score = reset_game()
    game_over = False

    while True:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_r:
                        snake, direction, next_direction, food, score = reset_game()
                        game_over = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                else:
                    if event.key == pygame.K_UP and direction != "DOWN":
                        next_direction = "UP"
                    elif event.key == pygame.K_DOWN and direction != "UP":
                        next_direction = "DOWN"
                    elif event.key == pygame.K_LEFT and direction != "RIGHT":
                        next_direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and direction != "LEFT":
                        next_direction = "RIGHT"

        # Update Game State
        if not game_over:
            direction = next_direction
            head = update_snake_position(snake, direction)

            if check_collisions(head, snake):
                game_over = True
            else:
                snake.insert(0, head)
                if head == food:
                    score += 1
                    food = spawn_food(snake)
                else:
                    snake.pop()

        # Render Graphics
        screen.fill((15, 15, 15))
        draw_grid(screen)
        draw_food(screen, food)
        draw_snake(screen, snake)
        draw_score(screen, font_small, score)

        if game_over:
            draw_game_over(screen, font_large, font_small, score)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
