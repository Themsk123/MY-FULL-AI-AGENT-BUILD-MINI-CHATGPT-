import random
from constants import WIDTH, HEIGHT, BLOCK_SIZE

def reset_game():
    """Resets snake position, direction, food, and score."""
    snake = [
        [100, 100],
        [80, 100],
        [60, 100]
    ]
    direction = "RIGHT"
    next_direction = "RIGHT"
    food = spawn_food(snake)
    score = 0
    return snake, direction, next_direction, food, score

def spawn_food(snake):
    """Spawns food at a random grid location not occupied by the snake."""
    while True:
        x = random.randrange(0, WIDTH, BLOCK_SIZE)
        y = random.randrange(0, HEIGHT, BLOCK_SIZE)
        food = [x, y]
        if food not in snake:
            return food

def update_snake_position(snake, direction):
    """Calculates and returns the new head position based on direction."""
    head = list(snake[0])
    if direction == "UP":
        head[1] -= BLOCK_SIZE
    elif direction == "DOWN":
        head[1] += BLOCK_SIZE
    elif direction == "LEFT":
        head[0] -= BLOCK_SIZE
    elif direction == "RIGHT":
        head[0] += BLOCK_SIZE
    return head

def check_collisions(head, snake):
    """Checks if the snake hit the walls or itself."""
    hit_wall = head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT
    hit_self = head in snake
    return hit_wall or hit_self
