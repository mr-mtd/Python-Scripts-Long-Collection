import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Define the Tetromino shapes
SHAPES = [
    [(0, 1), (1, 1), (2, 1), (3, 1)],  # I shape
    [(0, 1), (1, 1), (2, 1), (2, 0)],  # L shape
    [(0, 1), (1, 1), (2, 1), (2, 2)],  # J shape
    [(1, 0), (2, 0), (1, 1), (2, 1)],  # O shape
    [(0, 1), (1, 1), (1, 0), (2, 0)],  # S shape
    [(0, 0), (1, 0), (1, 1), (2, 1)],  # Z shape
    [(0, 1), (1, 1), (1, 0), (2, 1)]   # T shape
]

# Define the colors of the Tetromino shapes
COLORS = [
    CYAN,
    BLUE,
    ORANGE,
    YELLOW,
    GREEN,
    PURPLE,
    RED
]

# Define the game loop
def game_loop():
    # Set up the game variables
    board = [[0 for _ in range(10)] for _ in range(20)]
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.5
    current_shape = random.choice(SHAPES)
    current_color = random.choice(COLORS)
    x = 4
    y = 0
    game_over = False

    # Start the game loop
    while not game_over:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if is_valid_move(board, current_shape, x - 1, y):
                        x -= 1
                if event.key == pygame.K_RIGHT:
                    if is_valid_move(board, current_shape, x + 1, y):
                        x += 1
                if event.key == pygame.K_DOWN:
                    if is_valid_move(board, current_shape, x, y + 1):
                        y += 1

        # Update the game state
        fall_time += clock.get_rawtime()
        clock.tick()
        if fall_time / 1000 >= fall_speed:
        if is_valid_move(board, current_shape, x, y + 1):
            y += 1
        else:
            place_shape(board, current_shape, x, y, current_color)
            rows_cleared = clear_rows(board)
            if rows_cleared:
                print(f"Cleared {rows_cleared} rows")
            current_shape = random.choice(SHAPES)
            current_color = random.choice(COLORS)
            x = 4
            y = 0
            if not is_valid_move(board, current_shape, x, y):
                game_over = True
        fall_time = 0

    # Draw the game screen
    screen.fill(BLACK)
    draw_board(screen, board)
    draw_shape(screen, current_shape, x, y, current_color)
    pygame.display.update()

# Clean up and exit the game
pygame.quit()
quit()


"""-------------------------------------

Check if a move is valid
def is_valid_move(board, shape, x, y):
for i, j in shape:
if not 0 <= x + i < 10 or not 0 <= y + j < 20 or board[y + j][x + i]:
return False
return True

Place a shape on the board
def place_shape(board, shape, x, y, color):
for i, j in shape:
board[y + j][x + i] = color

Clear full rows on the board
def clear_rows(board):
rows_cleared = 0
for i, row in enumerate(board):
if all(row):
board.pop(i)
board.insert(0, [0 for _ in range(10)])
rows_cleared += 1
return rows_cleared

Draw the game board
def draw_board(screen, board):
for i, row in enumerate(board):
for j, cell in enumerate(row):
if cell:
pygame.draw.rect(screen, cell, (j * 30, i * 30, 30, 30), 0)
else:
pygame.draw.rect(screen, WHITE, (j * 30, i * 30, 30, 30), 1)

Draw a Tetromino shape
def draw_shape(screen, shape, x, y, color):
for i, j in shape:
pygame.draw.rect(screen, color, ((x + i) * 30, (y + j) * 30, 30, 30), 0)

Start the game loop
game_loop()




This example implements the basic mechanics of Tetris using Pygame. The game loop runs continuously and handles user input, updates the game state, and draws the game screen. The `is_valid_move` function checks if a move is valid, the `place_shape` function places a Tetromino shape on the board, and the `clear_rows` function clears full rows on the board. The `draw_board` function draws the game board, and the `draw_shape` function draws a Tetromino shape on the screen.

This code should give you a good starting point to create your own Tetris game in Python using Pygame. You can expand upon it by adding more shapes, levels, and game mechanics.


"""