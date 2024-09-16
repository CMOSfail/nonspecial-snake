import pygame
import sys
import random
import json
import os

# Load settings from the settings.json file
def load_settings():
    """
    Loads the game settings from the 'settings.json' file.
    If the file doesn't exist or settings are missing, default values are used.
    """
    default_settings = {
        "bombs_enabled": True,
        "bomb_behavior": 2,
        "golden_apple_enabled": True,
        "golden_apple_duration": 10,
        "speed_percentage": 100,
        "screen_width": 1280,
        "screen_height": 720
    }
    if os.path.exists('settings.json'):
        with open('settings.json', 'r') as f:
            settings = json.load(f)
        # Ensure all settings are present
        for key in default_settings:
            if key not in settings:
                settings[key] = default_settings[key]
        return settings
    else:
        # Create a default settings file if it doesn't exist
        with open('settings.json', 'w') as f:
            json.dump(default_settings, f, indent=4)
        return default_settings

# Load game settings
settings = load_settings()

# Initialize pygame
pygame.init()

# Screen dimensions
# Enforce minimum resolution of 1280x720 pixels
SCREEN_WIDTH = max(settings.get("screen_width", 1280), 1280)
SCREEN_HEIGHT = max(settings.get("screen_height", 720), 720)
CELL_SIZE = 20  # Size of each grid cell in pixels

# Grid dimensions (number of cells in the grid)
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE

# Colors (RGB format)
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)    # Snake color
RED = (220, 20, 60)      # Regular apple color
GOLD = (255, 215, 0)     # Golden apple color
BLACK = (0, 0, 0)
GRAY = (105, 105, 105)   # Bomb color
BACKGROUND_COLOR = (50, 50, 50)  # Background color

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('very non-special snake game!!!1!')

# Clock to control the game's frame rate
clock = pygame.time.Clock()

# Font for displaying text
font = pygame.font.SysFont('Arial', 25)

def draw_text(text, color, x, y, center=False):
    """
    Draws text on the screen at the specified position.

    Parameters:
    - text (str): The text to display.
    - color (tuple): The color of the text.
    - x (int): The x-coordinate.
    - y (int): The y-coordinate.
    - center (bool): Whether to center the text at (x, y).
    """
    img = font.render(text, True, color)
    rect = img.get_rect()
    if center:
        rect.center = (x, y)
        screen.blit(img, rect)
    else:
        screen.blit(img, (x, y))

def start_screen():
    """
    Displays the start screen with game information and instructions.
    Waits for the player to press ENTER to start the game.
    """
    screen.fill(BACKGROUND_COLOR)
    title_font = pygame.font.SysFont('Arial', 50, bold=True)
    title_text = title_font.render('very non-special snake game!!!1!', True, GOLD)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(title_text, title_rect)

    # Developer and Git repo
    draw_text('Developer: Itamar Itzhaki', WHITE, SCREEN_WIDTH // 2, 160, center=True)
    draw_text('Git Repo: https://github.com/CMOSfail/nonspecial-snake', WHITE, SCREEN_WIDTH // 2, 190, center=True)

    # Instructions
    instructions = [
        'Instructions:',
        'Objective: Control the snake to eat apples and grow longer.',
        'Controls:',
        '- Move Left: Arrow Left or \'A\'',
        '- Move Right: Arrow Right or \'D\'',
        '- Move Up: Arrow Up or \'W\'',
        '- Move Down: Arrow Down or \'S\'',
        '- Pause Game: Space Bar',
        '- Exit to Start Screen: Esc Key',
        'Special Items:',
        '- Golden Apples: Grant extra points and length.',
        '- Bombs: Avoid them! Depending on settings, they can either',
        '  end the game or cut your length in half.',
    ]

    y_offset = 240  # Starting y-position for instructions
    for line in instructions:
        draw_text(line, WHITE, SCREEN_WIDTH // 2, y_offset, center=True)
        y_offset += 30  # Adjust spacing between lines

    # Prompt to start the game
    draw_text('Press ENTER to play!!!', RED, SCREEN_WIDTH // 2, y_offset + 40, center=True)

    pygame.display.flip()

    # Wait for player to press ENTER
    waiting = True
    while waiting:
        clock.tick(15)  # Limit the frame rate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False

def game_over_screen(score):
    """
    Displays the game over screen with the final score.
    Provides options to restart or exit the game.
    """
    screen.fill(BACKGROUND_COLOR)
    draw_text('Game Over!', RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60, center=True)
    draw_text(f'Score: {score}', WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20, center=True)
    draw_text('Press Enter to Play Again or Esc to Exit', WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20, center=True)
    pygame.display.flip()

    # Wait for player input
    waiting = True
    while waiting:
        clock.tick(15)  # Limit the frame rate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                    main()  # Restart the game
                elif event.key == pygame.K_ESCAPE:
                    waiting = False
                    start_screen()  # Return to start screen
                    main()  # Start a new game

def pause_screen():
    """
    Displays the pause screen and waits for the player to resume or exit.
    """
    draw_text('Game Paused', RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20, center=True)
    draw_text('Press Space to Resume or Esc to Exit', WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20, center=True)
    pygame.display.flip()

    paused = True
    while paused:
        clock.tick(15)  # Limit the frame rate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                paused = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False  # Resume the game
                elif event.key == pygame.K_ESCAPE:
                    paused = False
                    start_screen()  # Return to start screen
                    main()  # Start a new game

def main():
    """
    The main function where the game loop resides.
    Initializes game variables and handles game logic.
    """
    # Load settings inside main to allow reloading after game over
    settings = load_settings()

    # Start Screen
    start_screen()

    # Initial snake position (center of the grid) and direction
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    snake_dir = (0, 0)  # Initial direction is stationary

    # Place the first regular apple on the grid
    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    # Golden apple variables
    golden_apple = None
    golden_apple_timer = 0
    golden_apple_duration = settings.get("golden_apple_duration", 10) * 10  # Duration in game ticks
    golden_apple_enabled = settings.get("golden_apple_enabled", True)

    # Game variables
    score = 0
    base_speed = 10  # Base speed of the game
    speed_percentage = settings.get("speed_percentage", 100) / 100
    speed = base_speed * speed_percentage
    apples_since_last_golden = 0  # Counter for golden apple spawning

    # Bomb variables
    bombs = []
    bomb_timer = 0
    bomb_interval = random.randint(50, 100)  # Bomb spawn interval in ticks
    bomb_duration = 50  # Duration bombs stay on the grid in ticks
    bombs_enabled = settings.get("bombs_enabled", True)
    bomb_behavior = settings.get("bomb_behavior", 2)  # 1: End game, 2: Cut length in half

    running = True  # Game loop control variable
    while running:
        clock.tick(speed)  # Control the game's speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            # Handle key presses for snake movement and game controls
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_a] and snake_dir != (1, 0):
                    snake_dir = (-1, 0)
                elif event.key in [pygame.K_RIGHT, pygame.K_d] and snake_dir != (-1, 0):
                    snake_dir = (1, 0)
                elif event.key in [pygame.K_UP, pygame.K_w] and snake_dir != (0, 1):
                    snake_dir = (0, -1)
                elif event.key in [pygame.K_DOWN, pygame.K_s] and snake_dir != (0, -1):
                    snake_dir = (0, 1)
                elif event.key == pygame.K_SPACE:
                    # Pause the game
                    pause_screen()
                elif event.key == pygame.K_ESCAPE:
                    # Exit to start screen
                    start_screen()
                    main()
                    return

        if snake_dir != (0, 0):
            # Check if snake is empty before moving
            if len(snake) == 0:
                game_over_screen(score)
                return

            # Calculate new head position with wrap-around
            new_head = ((snake[0][0] + snake_dir[0]) % GRID_WIDTH,
                        (snake[0][1] + snake_dir[1]) % GRID_HEIGHT)

            # Check for self-collision
            if new_head in snake:
                game_over_screen(score)
                return

            # Insert the new head at the beginning of the snake list
            snake.insert(0, new_head)

            # Check collision with bombs
            if bombs_enabled and new_head in [bomb['position'] for bomb in bombs]:
                if bomb_behavior == 1:
                    # Collision with bomb ends the game
                    game_over_screen(score)
                    return
                elif bomb_behavior == 2:
                    # Cut the snake's length in half (minimum length of 1)
                    new_length = max(1, len(snake) // 2)
                    snake = snake[:new_length]
                    # Remove the bomb from the grid
                    bombs = [bomb for bomb in bombs if bomb['position'] != new_head]

            # Check if regular apple is eaten
            if new_head == food:
                score += 1
                apples_since_last_golden += 1
                # Increase speed every 5 points
                if score % 5 == 0:
                    speed += 1 * speed_percentage

                # Place a new regular apple
                while True:
                    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
                    if (food not in snake and food != golden_apple and
                        food not in [bomb['position'] for bomb in bombs]):
                        break

                # Decide whether to spawn a golden apple
                if (golden_apple_enabled and apples_since_last_golden >= random.randint(1, 10)
                        and golden_apple is None):
                    # Place a golden apple
                    while True:
                        golden_apple = (random.randint(0, GRID_WIDTH - 1),
                                        random.randint(0, GRID_HEIGHT - 1))
                        if (golden_apple not in snake and golden_apple != food and
                            golden_apple not in [bomb['position'] for bomb in bombs]):
                            break
                    golden_apple_timer = golden_apple_duration
                    apples_since_last_golden = 0

            # Check if golden apple is eaten
            elif golden_apple_enabled and golden_apple and new_head == golden_apple:
                score += 2
                # Grow the snake by an extra segment
                snake.insert(0, new_head)
                if score % 5 == 0:
                    speed += 1 * speed_percentage
                golden_apple = None
                golden_apple_timer = 0

            else:
                # Remove the tail segment if the snake's length is greater than 1
                if len(snake) > 1:
                    snake.pop()
                else:
                    # If the snake's length is 1, do not remove the tail segment
                    pass

            # Bomb appearance logic
            if bombs_enabled:
                bomb_timer += 1
                if bomb_timer >= bomb_interval:
                    bomb_timer = 0
                    bomb_interval = random.randint(50, 100)  # Reset bomb interval
                    # Add a new bomb
                    while True:
                        bomb_pos = (random.randint(0, GRID_WIDTH - 1),
                                    random.randint(0, GRID_HEIGHT - 1))
                        if (bomb_pos not in snake and bomb_pos != food and
                            bomb_pos != golden_apple and
                            bomb_pos not in [bomb['position'] for bomb in bombs]):
                            bombs.append({'position': bomb_pos, 'timer': bomb_duration})
                            break

                # Update bombs
                for bomb in bombs[:]:
                    bomb['timer'] -= 1
                    if bomb['timer'] <= 0:
                        bombs.remove(bomb)  # Remove bomb when timer expires

            # Update golden apple timer
            if golden_apple_enabled and golden_apple:
                golden_apple_timer -= 1
                if golden_apple_timer <= 0:
                    golden_apple = None  # Remove golden apple when timer expires
                    golden_apple_timer = 0

        # Drawing section
        screen.fill(BACKGROUND_COLOR)  # Clear the screen

        # Draw the snake
        for segment in snake:
            rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE,
                               CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GREEN, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)  # Draw outline

        # Draw regular apple
        food_rect = pygame.Rect(food[0] * CELL_SIZE, food[1] * CELL_SIZE,
                                CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, RED, food_rect)

        # Draw golden apple if it exists
        if golden_apple_enabled and golden_apple:
            golden_rect = pygame.Rect(golden_apple[0] * CELL_SIZE,
                                      golden_apple[1] * CELL_SIZE,
                                      CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GOLD, golden_rect)

        # Draw bombs
        if bombs_enabled:
            for bomb in bombs:
                bomb_rect = pygame.Rect(bomb['position'][0] * CELL_SIZE,
                                        bomb['position'][1] * CELL_SIZE,
                                        CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, GRAY, bomb_rect)
                pygame.draw.rect(screen, BLACK, bomb_rect, 1)  # Draw outline

        # Draw the score on the screen
        draw_text(f'Score: {score}', WHITE, 10, 10)

        # Update the display
        pygame.display.flip()

    # Quit pygame
    pygame.quit()

# Run the game
if __name__ == '__main__':
    main()
