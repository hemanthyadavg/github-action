import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
width, height = 640, 480
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the clock
clock = pygame.time.Clock()

# Set up the snake and food
snake_block_size = 20
snake_speed = 15

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 50)


def our_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, GREEN, [x[0], x[1], snake_block_size, snake_block_size])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [width / 6, height / 3])


def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = width / 2
    y1 = height / 2

    # Change in position of the snake
    x1_change = 0
    y1_change = 0

    # Initial length of the snake
    snake_list = []
    length_of_snake = 1

    # Generate random coordinates for the food
    food_x = round(random.randrange(0, width - snake_block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - snake_block_size) / 20.0) * 20.0

    while not game_over:
        while game_close:
            display.fill(BLACK)
            message("You lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            # Check for user input to quit or restart the game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handle arrow key inputs to change the snake's direction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        # Check if the snake hits the boundaries of the display
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change

        display.fill(BLACK)
        pygame.draw.rect(display, RED, [food_x, food_y, snake_block_size, snake_block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Remove the tail of the snake if it gets too long
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake hits itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake on the display
        our_snake(snake_block_size, snake_list)

        pygame.display.update()

        # Check if the snake eats the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - snake_block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - snake_block_size) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()


# Start the game loop
game_loop()
