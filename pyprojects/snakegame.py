import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants for the game (setup)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 20  # Size of each grid cell (snake/food are this size)
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE  # Number of grids horizontally
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE  # Vertically

# Colors (RGB)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)  # Snake color
RED = (255, 0, 0)    # Food color
WHITE = (255, 255, 255)  # Text color

# Directions (as vectors for movement)
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling speed
clock = pygame.time.Clock()
SPEED = 10  # Frames per second (updates per second)

# Font for score and game over text
font = pygame.font.SysFont(None, 35)

def draw_snake(snake):
    """Draw the snake on the screen."""
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_food(food):
    """Draw the food on the screen."""
    pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def show_score(score):
    """Display the score in the top-left."""
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def game_over_message(score):
    """Display game over message in the center."""
    text = font.render(f"Game Over! Score: {score}", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

def main():
    # Initial snake position (list of (x, y) grid coords, starting in center)
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]  # Single segment to start
    
    # Grow the snake initially to length 3 (add segments behind)
    for i in range(2):
        snake.append((snake[-1][0] - 1, snake[-1][1]))  # Add to left

    # Initial direction
    direction = RIGHT

    # Initial food position (random, not on snake)
    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    while food in snake:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    # Score
    score = 0

    # Game loop
    running = True
    game_over = False
    while running:
        # Handle events (input)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT
                elif event.key == pygame.K_ESCAPE:  # Quit on ESC
                    running = False

        if not game_over:
            # Update snake position
            head = snake[0]
            new_head = (head[0] + direction[0], head[1] + direction[1])

            # Check wall collisions
            if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
                new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
                game_over = True
                continue

            # Check self-collision
            if new_head in snake:
                game_over = True
                continue

            # Add new head
            snake.insert(0, new_head)

            # Check if ate food
            if new_head == food:
                score += 1
                # Place new food (not on snake)
                food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
                while food in snake:
                    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            else:
                # Remove tail if not eating
                snake.pop()

        # Drawing
        screen.fill(BLACK)  # Clear screen
        draw_snake(snake)
        draw_food(food)
        show_score(score)

        if game_over:
            game_over_message(score)

        pygame.display.flip()  # Update display

        # Control speed
        clock.tick(SPEED)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()