import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLACK = (0, 0, 0)

# Set display dimensions
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# Create display
game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Snake Game')

# Set up clock for controlling the frame rate
clock = pygame.time.Clock()

# Set snake and food dimensions
SNAKE_BLOCK = 20
FOOD_BLOCK = 20
SNAKE_SPEED = 15

# Font styles
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [DISPLAY_WIDTH / 6, DISPLAY_HEIGHT / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = DISPLAY_WIDTH / 2
    y1 = DISPLAY_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, DISPLAY_WIDTH - FOOD_BLOCK) / 20.0) * 20.0
    foody = round(random.randrange(0, DISPLAY_HEIGHT - FOOD_BLOCK) / 20.0) * 20.0

    while not game_over:

        while game_close == True:
            game_display.fill(BLACK)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        if x1 >= DISPLAY_WIDTH or x1 < 0 or y1 >= DISPLAY_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        game_display.fill(BLACK)
        pygame.draw.rect(game_display, RED, [foodx, foody, FOOD_BLOCK, FOOD_BLOCK])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(SNAKE_BLOCK, snake_List)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, DISPLAY_WIDTH - FOOD_BLOCK) / 20.0) * 20.0
            foody = round(random.randrange(0, DISPLAY_HEIGHT - FOOD_BLOCK) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

gameLoop()
